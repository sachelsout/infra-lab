# Day 27 – Kubernetes Readiness and Liveness Probes

This project demonstrates how to use **readiness** and **liveness probes** in Kubernetes with a FastAPI application.

---

## 📁 Folder Structure

```plaintext
k8s-probes-demo/
├── app/
│ ├── main.py # FastAPI application with readiness & liveness endpoints
│ └── requirements.txt # FastAPI dependency
├── Dockerfile # Docker image definition
├── deployment.yaml # Kubernetes Deployment with readiness and liveness probes
├── service.yaml # Kubernetes Service (NodePort)
└── README.md # Documentation (this file)
```

---

## 🚀 Features

- ✅ FastAPI web server with Swagger UI
- ✅ `/` – root endpoint
- ✅ `/healthz` – returns app status for Kubernetes liveness probe
- ✅ `/readyz` – returns app status for Kubernetes readiness probe
- ✅ Kubernetes configuration with both probes defined
- ✅ Exposed via a NodePort service

---

## 🐳 Build & Push Docker Image

Make sure Docker is running and you're logged in to Docker Hub.

```bash
docker build -t rohan2304/k8s-probes-demo .
docker push rohan2304/k8s-probes-demo
```

## ☸️ Deploy to Kubernetes

Apply the Kubernetes manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## 🌐 Access in Browser

Check which NodePort was assigned:

```bash
kubectl get svc
```

Example output:

```pgsql
NAME              TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
k8s-probes-demo   NodePort   10.96.200.20    <none>        80:31234/TCP   1m
```

Visit your app in the browser:

```arduino
http://localhost:31234/docs
```

You’ll see FastAPI's interactive Swagger UI.

## 🔍 Test Probes

Check health manually:

- Liveness: ```http://localhost:31234/healthz```

- Readiness: ```http://localhost:31234/readyz```

Expected output:

```json
{"status": "ok"}
```

```json
{"status": "true"}
```

## ✅ Expected Behavior

- Liveness probe ensures the container is healthy and restarts it if it crashes.

- Readiness probe waits before traffic is routed to the container (until it's ready).

## 🧼 Cleanup

To remove everything:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

## 🛠️ Tech Stack

- FastAPI

- Docker

- Kubernetes (via Docker Desktop)

- Swagger UI for API docs

## ✅ Outcome

You deployed a FastAPI app on Kubernetes, added liveness and readiness probes, verified them via Swagger UI and browser, and tested their behavior.