# 📈 FastAPI App with Prometheus Monitoring (Day 13)

This project demonstrates how to monitor a FastAPI application using Prometheus. The FastAPI app is instrumented to expose performance metrics, which Prometheus scrapes and displays.

## 🧱 Tech Stack

- FastAPI

- Docker + Docker Compose

- Prometheus

- prometheus-fastapi-instrumentator for metrics

## 📂 Folder Structure

```bash
prometheus-monitoring/
├── app/
│   └── main.py
├── prometheus/
│   └── prometheus.yml
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 🚀 Running the App

### Step 1: Build and start containers

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-2/prometheus-monitoring

docker compose up --build
```

### Step 2: Access the services

- 📱 FastAPI app: http://localhost:8000

- 📊 Metrics endpoint: http://localhost:8000/metrics

- 📈 Prometheus UI: http://localhost:9090

## 🧪 Example Prometheus Query

Inside the Prometheus UI, try this query to monitor HTTP requests:

```nginx
http_requests_total
```

Or to view response times:

```nginx
http_request_duration_seconds_count
```

## 🛠️ Code Highlights

### 🔧 ```main.py```

```python
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

# Add instrumentation
Instrumentator().instrument(app).expose(app)
```

### ⚙️ ```prometheus/prometheus.yml```

```yaml
global:
  scrape_interval: "5s"

scrape_configs:
  - job_name: "fastapi-app"
    static_configs:
      - targets: ["app:8000"]
```

### 🐳 ```docker-compose.yml```

```yaml
version: '3.8'

services:
  app:
    build: ./app
    ports:
      - "8000:8000"

  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
```

## ✅ Outcome

You now have a fully functional monitoring setup for FastAPI with Prometheus — perfect for production observability and performance tuning.