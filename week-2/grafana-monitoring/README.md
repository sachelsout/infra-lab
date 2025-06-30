# 📊 FastAPI Monitoring with Prometheus & Grafana

This project demonstrates how to monitor a FastAPI application using Prometheus and Grafana. You'll see live metrics like request count and visualize them in real-time dashboards.

## 📥 Clone This Project

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-2/grafana-monitoring
```

## 🧱 Tech Stack

- FastAPI — Web framework for the app

- Prometheus — Metrics collection and storage

- Grafana — Metrics visualization

- Docker Compose — Container orchestration

## 📁 Folder Structure

```bash
grafana-monitoring/
 ├── fastapi-app/
 │   ├── main.py                # FastAPI app with  Prometheus metrics
 │   ├── requirements.txt       # Dependencies
 │   └── Dockerfile             # Build FastAPI container
 ├── prometheus/
 │   └── prometheus.yml         # Prometheus configuration
 ├── grafana/
 │   ├─ dashboards/
 |   |    ├── json
 |   |    |     └── fastapi-dashboard.json
 │   │    ├── dashboard.yml     # Grafana dashboard provisioning
 |   │    └── default.yaml 
 │   └── datasources
 |        └── datasources.yml
 ├── docker-compose.yml         # Runs FastAPI + Prometheus + Grafana
 └── README.md                  # This file
```

## 🚀 How to Run

1. Start all services
    ```bash
    docker-compose up --build
    ```

2. Access the services
    - FastAPI App: http://localhost:8000

    - FastAPI Metrics: http://localhost:8000/metrics

    - Prometheus UI: http://localhost:9090

    - Grafana Dashboard: http://localhost:3000

        - Username: ```admin```

        - Password: ```admin```

## 📈 Dashboard Details

The Grafana dashboard displays:

- 🔢 ```app_requests_total``` — Total requests made to the FastAPI app

- ⚙️ Built-in Python metrics (```process_```, ```python_```, etc.)

If you don't see data immediately, trigger some requests (e.g., visit http://localhost:8000).

## 📝 Notes

- Prometheus scrapes the app every 5 seconds (```scrape_interval: "5s"```).

- Metrics are exposed using ```prometheus_client```.

- Grafana auto-loads dashboards via provisioning (```dashboard.yml``` + ```dashboard.json```).