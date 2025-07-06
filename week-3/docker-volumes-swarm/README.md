# 💾 Docker Volumes in Swarm (Day 19)

This project demonstrates how to persist uploaded files in a FastAPI app using **named Docker volumes** on **Docker Swarm**.

---

## 📁 Folder Structure

```plaintext
docker-volumes-swarm/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-stack.yml
└── README.md
```

## 🚀 Features
- 📤 FastAPI-based file upload API.

- 💾 Persistent file storage using Docker named volumes.

- ⚙️ Swarm deployment using docker stack deploy.

## ⚙️ FastAPI App

### `main.py`:

```python
from fastapi import FastAPI, UploadFile, File
import os
import shutil

app = FastAPI()
UPLOAD_DIR = "/app/uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"file '{file.filename}' saved"}
```

- Files are saved to `/app/uploaded_files`, which maps to a named volume.

### 🐋 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### `docker-stack.yml`
```yaml
version: "3.8"

services:
  file-uploader:
    image: rohan2304/file-upload-volume:latest
    ports:
      - "8000:8000"
    volumes:
      - uploaded_data:/app/uploaded_files
    deploy:
      replicas: 1

volumes:
  uploaded_data:
```

- The `uploaded_data` volume ensures files are not lost when containers restart or migrate.

## 🔧 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-3/docker-volumes-swarm
```

### 2. Build & Push Docker Image

```bash
cd app
docker build -t rohan2304/file-upload-volume:latest .
docker push rohan2304/file-upload-volume:latest
```

### 3. Deploy to Docker Swarm

```bash
cd ..
docker stack deploy -c docker-stack.yml fileupload
```

### 4. Upload a File (Two Options)

#### a. Swagger UI

- Open http://localhost:8000/docs

- Use the `/upload` endpoint

#### b. cURL

```bash
curl -F "file=@test.jpg" http://localhost:8000/upload
```

## 📊 What This Teaches

- How to use Docker named volumes in Swarm.

- How to persist uploaded files in a containerized app.

- How to build simple stateful services with Docker Swarm.

## 🧹 Cleanup

### 🔻 Remove the Docker Stack

```bash
docker stack rm fileupload
```

This stops and removes all services, networks, and volumes created by the stack.

### 🔥 Remove the Named Volume (if needed)

#### ⚠️ Be careful — this deletes all uploaded files inside the volume!

```bash
docker volume rm uploaded_data
```

Check if it's removed:

```bash
docker volume ls
```

### 🧼 (Optional) Remove the Docker Image

```bash
docker rmi rohan2304/file-upload-volume:latest
```

Use this only if you want to clean up your local image cache.