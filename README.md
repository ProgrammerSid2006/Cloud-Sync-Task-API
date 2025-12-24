Cloud-Sync Task Orchestrator 🚀
📌 Overview
This project is a high-performance RESTful API designed to bridge local task management with cloud-scale data persistence.  

🛠 Technical Stack

Language: Python 3.10+    


Framework: FastAPI (Asynchronous ASGI)    


Database: Google Cloud Firestore (NoSQL)    


Validation: Pydantic (Data Integrity)    

Security: Firebase Admin SDK (Service Account Authentication)

🚀 Installation & Setup
Clone the Repository:

Bash

git clone https://github.com/ProgrammerSid2006/Task-Orchestrator.git
cd Task-Orchestrator
Install Dependencies:

Bash

pip install fastapi uvicorn firebase-admin pydantic
Configure Google Cloud Credentials:

Place your serviceAccountKey.json in the root directory.

Security Note: This file is excluded via .gitignore to prevent credential leakage.

🧪 How to Verify (Verification Steps)
This API includes built-in interactive documentation for instant verification of cloud synchronization.

1. Launch the Server
Bash

python -m uvicorn main:app --reload
2. Verify via Interactive Docs (Swagger UI)
Step A: Navigate to http://127.0.0.1:8000/docs in your browser.

Step B (POST): Expand the POST /tasks/ endpoint. Click "Try it out", enter your task JSON, and hit Execute.

Step C (Cloud Check): Open your Firebase Console. [cite_start]You will see the record synced to the Firestore Database in real-time.   

Step D (GET): Copy the id from the response. [cite_start]Expand the GET /tasks/{task_id} endpoint, paste the ID, and verify the sub-second retrieval directly from Google Cloud.   

📈 Key Engineering Concepts Implemented
[cite_start]

Real-Time Sync: Leveraged Google Cloud Firestore for schema-less, real-time data persistence.   


Performance Optimization: Utilized async methods to handle concurrent requests with sub-second latency.   


Professional API Design: Implemented standardized JSON response structures and HTTP status codes.
