# 🚑 Docker Swarm Healthcheck & Restart Policy (Day 18)

This project demonstrates how to implement healthchecks and restart policies for services deployed on Docker Swarm using a FastAPI app.

---

## 📁 Folder Structure

```plaintext
swarm-healthcheck-restart-policies/
├── app/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
├── docker-stack.yml
└── README.md
```


---

## 🚀 Features

- 🐳 Deploy FastAPI app on Docker Swarm.
- ❤️ Implement a `/health` endpoint to simulate flaky health behavior.
- 🔁 Configure **restart policy** in `docker-stack.yml` to restart on failure.
- ✅ Observe how Swarm reacts to failing healthchecks and restarts the container.

---

## 📦 FastAPI App

**`main.py`**:

```python
from fastapi import FastAPI, Response, status
import time
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Docker Swarm!"}

@app.get("/health")
def health_check(response: Response):
    if random.random() < 0.8:
        return {"status": "healthy"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "unhealthy"}
```

- The ```/health``` endpoint randomly returns healthy or unhealthy responses to simulate real-world flaky services.

## 🐋 Dockerfile

**`Dockerfile`**:

```Dockerfile
FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl bash && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📄 `docker-stack.yml`
```yaml
version: "3.8"

services:
  fastapi-app:
    image: rohan2304/fastapi-healthcheck:latest  # Replace with your actual image if needed
    ports:
      - "8000:8000"
    deploy:
      replicas: 1
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
        window: 30s
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 3s
      retries: 3
```

---

## 🔧 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-3/swarm-healthcheck-restart-policies 
```

### 2. Build & Push Docker Image
```bash
docker build -t rohan2304/fastapi-healthcheck:latest .
docker push rohan2304/fastapi-healthcheck:latest
```

### 3. Deploy to Docker Swarm
```bash
docker stack deploy -c docker-stack.yml fastapiapp
```

### 4. Check Status
```bash
docker service ps fastapiapp_fastapi-app
docker service logs fastapiapp_fastapi-app
```

## 📊 What This Teaches

- How to simulate and monitor service health in production-like environments.

- How Docker Swarm handles service failures using healthchecks and restart policies.

- How to structure production-ready Dockerfiles and stack configs.