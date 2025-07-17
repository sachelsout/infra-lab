# Day 26 – Kubernetes File Upload App Deployment with FastAPI

On Day 26 of the 3-month Infrastructure/Production Engineering plan, we containerized and deployed a FastAPI-based file upload application to Kubernetes using a `Deployment` and `Service`. We also added an API endpoint to list all uploaded files, verified functionality via browser/Postman, and ensured cleanup works.

## 🚀 Features Implemented

- Upload files through a `/upload` endpoint.

- List all previously uploaded files using a `/files` endpoint.

- Containerized FastAPI app using Docker.

- Created Kubernetes `Deployment` and `Service` to run the app.

- Exposed the app using a `NodePort` service for local access.

- Verified file upload and retrieval.

- Used absolute path (`/app/uploads`) for consistent behavior inside container.

- Cleaned up all Kubernetes resources at the end.

## 📂 Folder Structure

```plaintext
k8s-file-upload-app/
├── Dockerfile
├── app/
│   ├── main.py
|   └── requirements.txt
├── deployment.yaml
├── service.yaml
└── README.md
```

## 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

## 🌐 Accessing the App

### Upload Files

```http
POST http://localhost:<NODEPORT>/upload
```

Use Postman or browser (with a form) to upload files.

### List Uploaded Files

```http
GET http://localhost:<NODEPORT>/files
```

Get back a list of filenames previously uploaded.

### 🔎 Example output:

```json
{
  "uploaded_files": ["example.png", "notes.txt"]
}
```

### 📌 Note:

Replace `<NODEPORT>` with the actual port shown from:

```bash
kubectl get svc
```

Example:

```bash
NAME              TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
fastapi-service   NodePort   10.100.48.73   <none>        80:31047/TCP   5m
```

In this case, use `http://localhost:30036`.

## 🧹 Cleanup

Delete all resources created:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

You can verify deletion using:

```bash
kubectl get all
```

## ✅ Status

All endpoints are tested and working:

- Upload file via POST `/upload`

- List uploaded files via GET `/files`

- Kubernetes deployment + service

- Cleanup tested and confirmed