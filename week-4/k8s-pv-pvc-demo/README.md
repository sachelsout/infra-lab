# 🗃️ Day 25 – Kubernetes PersistentVolumes and PersistentVolumeClaims (FastAPI Notes App)

This project demonstrates the use of **PersistentVolumes (PV)** and **PersistentVolumeClaims (PVC)** in Kubernetes with a simple FastAPI notes app. The app writes and reads notes from a file stored in a persistent volume, ensuring data survives pod restarts.

---

## 📁 Folder Structure

```plaintext
k8s-pv-pvc-demo/
│
├── app/
│ └── main.py # FastAPI app with endpoints to write/read notes
│
├── Dockerfile # Builds the FastAPI image
├── deployment.yaml # Kubernetes Deployment with volume mount
├── pv.yaml # PersistentVolume definition
├── pvc.yaml # PersistentVolumeClaim definition
├── service.yaml # NodePort Service to expose the app
└── README.md # You're here!
```


---

## ⚙️ Setup Instructions

### 1. ✅ Prerequisite

Make sure Kubernetes is enabled in Docker Desktop:

> Docker Desktop → Settings → Kubernetes → Enable Kubernetes

---

### 2. 🛠️ Build and push Docker Image to docker hub

```bash
docker build -t <docker-username>/k8s-pv-pvc-demo:latest .
docker push <docker-username>/k8s-pv-pvc-demo:latest
```

### 3. 🚀 Deploy to Kubernetes

```bash
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 4. 📡 Access the FastAPI App

Find the `NodePort`:

```bash
kubectl get svc
```

Then visit:

```arduino
http://localhost:<NodePort>
```

## 🧪 Usage

### ➕ Add a Note

```bash
curl -X POST "http://localhost:<NodePort>/write?note=hello-k8s"
```

### 📖 View Saved Notes

```bash
curl "http://localhost:<NodePort>/read"
```

All notes are saved to `/data/notes.txt` inside the container, backed by a persistent volume.

## 🧹 Cleanup

To delete all created resources:

```bash
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
kubectl delete -f pvc.yaml
kubectl delete -f pv.yaml
```

Confirm cleanup:

```bash
kubectl get all
kubectl get pvc
kubectl get pv
```

## 🛠️ Tech Stack

- 🐍 FastAPI

- 🐳 Docker

- ☸️ Kubernetes (Docker Desktop)