from fastapi import FastAPI, HTTPException
import firebase_admin
from firebase_admin import credentials, firestore
from pydantic import BaseModel
from typing import Optional

# 1. Initialize Google Firebase (GCP NoSQL)
# You will get this JSON key from the Firebase Console
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

@app.post("/tasks/")
async def create_task(task: Task):
    """Create a task in the Cloud Firestore database"""
    task_data = task.dict()
    # Add to Google Cloud Firestore
    update_time, task_ref = db.collection("tasks").add(task_data)
    return {"id": task_ref.id, "status": "Task created in Cloud"}

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    """Retrieve a specific task from the cloud"""
    task_ref = db.collection("tasks").document(task_id)
    doc = task_ref.get()
    if doc.exists:
        return doc.to_dict()
    raise HTTPException(status_code=404, detail="Task not found")