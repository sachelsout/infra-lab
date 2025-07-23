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

## 🛠️ Week 4: Kubernetes Basics
| Day | Project | Description |
|-----|---------|-------------|
| 22 | [k8s-first-pod](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-first-pod) | Deployed a single NGINX container in Kubernetes using Docker Desktop's built-in K8s cluster. |
| 23 | [k8s-fastapi-demo](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-fastapi-demo) | Deployed a simple FastAPI app to a Kubernetes cluster using Docker Desktop's built-in Kubernetes. |
| 24 | [k8s-configmap-secret-demo](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-configmap-secret-demo) | Using ConfigMaps and Secrets in Kubernetes to inject configuration and sensitive data into a FastAPI application. |
| 25 | [k8s-pv-pvc-demo](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-pv-pvc-demo) | Using PersistentVolumes (PV) and PersistentVolumeClaims (PVC) in Kubernetes with a simple FastAPI notes app. |
| 26 | [k8s-file-upload-app](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-file-upload-app) | Deployed a fastAPI-based file upload application to Kubernetes using a Deployment and Service. |
| 27 | [k8s-probes-demo](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-probes-demo) | Using readiness and liveness probes in Kubernetes with a FastAPI application. |
| 28 | [k8s-dashboard-monitoring](https://github.com/sachelsout/infra-lab/tree/main/week-4/k8s-dashboard-monitoring) | Set up and use the Kubernetes Dashboard to monitor the FastAPI app (k8s-probes-demo) we built on Day 27. |

---

## 🛠️ Week 5: Helm, Advanced K8s, Ingress, GitOps
| Day | Project | Description |
|-----|---------|-------------|
| 29 | [helm-redis-install](https://github.com/sachelsout/infra-lab/tree/main/week-5/helm-redis-install) | Helm Basics: Deploying Redis on Kubernetes. |
| 30 | [helm-fastapi-app](https://github.com/sachelsout/infra-lab/tree/main/week-5/helm-fastapi-app) | Deploying FastAPI File Upload App on Kubernetes using Helm. |

---

## 🌱 Upcoming Topics

- Secure Docker image practices
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
