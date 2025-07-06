# 🧱 infra-lab: My 3-Month Infra Engineering Journey

This repository documents my **3-month journey to learn Infrastructure Engineering** through a series of hands-on projects. Each folder represents a day's dedicated project, starting from Docker fundamentals to integrating databases, CI/CD, and more.

---

## ✅ Week 1: Docker, Flask, Redis, Postgres Basics

| Day | Project | Description |
|-----|---------|-------------|
| 1 | [flask-docker-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/flask-docker-app) | A simple Flask web app containerized using Docker. |
| 2 | [flask-ml-docker-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/flask-ml-docker-app) | ML model (Logistic Regression) exposed via Flask, containerized using Docker. |
| 3 | [flask-redis-compose-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/flask-redis-compose-app) | Counter app using Flask + Redis with Docker Compose. |
| 4 | [flask-redis-volume-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/flask-redis-volume-app) | Redis app with Docker volume for data persistence. |
| 5 | [postgres-flask-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/postgres-flask-app) | Flask + PostgreSQL web app with Docker Compose. |
| 6 | [file-upload-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/file-upload-app) | File upload and serve app using bind mounts. |
| 7 | [static-file-server](https://github.com/sachelsout/infra-lab/tree/main/week-1/static-file-server) | Static file server with Flask and bind mounts. |

---

## 🚧 Week 2: Reverse Proxy, Linux CLI, CI/CD

| Day | Project | Description |
|-----|---------|-------------|
| 8 | [fastapi-nginx-reverse-proxy](https://github.com/sachelsout/infra-lab/tree/main/week-2/fastapi-nginx-reverse-proxy) | NGINX reverse proxy to FastAPI/Flask app + healthchecks. |
| 9 | [linux-basics-part1](https://github.com/sachelsout/infra-lab/tree/main/week-2/linux-basics-part1) | Learned essential Linux commands, navigation, and scripting basics. |
| 10 | [linux-basics-part2](https://github.com/sachelsout/infra-lab/tree/main/week-2/linux-basics-part2) | Advanced bash, piping, redirection, file permissions, and processes. |
| 11 | [file-upload-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/file-upload-app) + [CI/CD README](https://github.com/sachelsout/infra-lab/tree/main/week-2/cicd-github-actions) | Implemented GitHub Actions for Docker build & push. |
| 12 | [file-upload-app](https://github.com/sachelsout/infra-lab/tree/main/week-1/file-upload-app) + [Advanced CI/CD README](https://github.com/sachelsout/infra-lab/tree/main/week-2/advanced-cicd) | Added automated tests + permission fixes using GitHub Actions. |
| 13 | [prometheus-monitoring](https://github.com/sachelsout/infra-lab/tree/main/week-2/prometheus-monitoring) | Prometheus setup for monitoring containers. |
| 14 | [grafana-monitoring](https://github.com/sachelsout/infra-lab/tree/main/week-2/grafana-monitoring) | Grafana dashboard to visualize metrics. |

---

## 🛠️ Week 3: Docker Swarm & Secrets Management

| Day | Project | Description |
|-----|---------|-------------|
| 15 | [docker-swarm-file-upload](https://github.com/sachelsout/infra-lab/tree/main/week-3/docker-swarm-file-upload) | Converted the file upload app to run on Docker Swarm using `docker stack deploy`. |
| 16 | [docker-secrets-env](https://github.com/sachelsout/infra-lab/tree/main/week-3/docker-secrets-env) | Managed secrets securely in Docker Swarm using `docker secret` and environment variables. |
| 17 | [docker-multi-host-networking](https://github.com/sachelsout/infra-lab/tree/main/week-3/docker-multi-host-networking) | Enable services to communicate across multiple Docker nodes. |
| 18 | [swarm-healthchecks-restart-policies](https://github.com/sachelsout/infra-lab/tree/main/week-3/swarm-healthchecks-restart-policies) | Implement healthchecks and restart policies for services deployed on Docker Swarm. |
| 19 | [docker-volumes-swarm](https://github.com/sachelsout/infra-lab/tree/main/week-3/docker-volumes-swarm) | Persist uploaded files in a FastAPI app using named Docker volumes on Docker Swarm. |
| 20 | [swarm-app-with-db](https://github.com/sachelsout/infra-lab/tree/main/week-3/swarm-app-with-db) | A simple blog backend built with FastAPI and PostgreSQL, containerized using Docker, and deployed using Docker Swarm. |
---

## 🌱 Upcoming Topics

- Secure Docker image practices
- Kubernetes fundamentals
- Ingress, load balancing
- Full-stack infra design

---

## 🔗 GitHub Repository

👉 [https://github.com/sachelsout/infra-lab](https://github.com/sachelsout/infra-lab)

---

## 🧑‍💻 Author

**Rohan Dawkhar**  
MS in Data Science @ University of Maryland  
Follow this repo for regular updates on my Infra Engineering journey.
