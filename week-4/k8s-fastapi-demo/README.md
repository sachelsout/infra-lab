# 📦 Day 23: Kubernetes Deployments and Services – FastAPI on K8s

Today, we deployed a simple FastAPI app to a Kubernetes cluster using Docker Desktop's built-in Kubernetes.

## 📁 Folder Structure

```graphql
k8s-fastapi-demo/
├── deployment.yaml       # Deployment config (2 replicas)
├── service.yaml          # NodePort service to expose the app
├── Dockerfile            # FastAPI app Dockerfile
└── app/
    └── main.py           # FastAPI app source code
```

## ⚙️ Step 1: Prepare the App
### `app/main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Kubernetes!"}
```

### `Dockerfile`

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY ./app /app
RUN pip install fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
```

## 🛠️ Step 2: Build & Push Docker Image

```bash
docker build -t rohan2304/k8s-fastapi-demo:latest .
docker push rohan2304/k8s-fastapi-demo:latest
```

## 📦 Step 3: Kubernetes Manifests
`deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: fastapi
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
      - name: fastapi
        image: rohan2304/k8s-fastapi-demo:latest
        ports:
        - containerPort: 5000
```

`service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: NodePort
  selector:
    app: fastapi
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
    nodePort: 30007
```

## 🚀 Step 4: Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## 🌐 Step 5: Access the App
Visit in browser:
```arduino
http://localhost:30007
```
Expected response:
```json
{"message": "Hello from Kubernetes!"}
```

## ✅ Step 6: Verify Everything

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

## 🧹 Cleanup (Optional)
To delete all resources created in this demo:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

Or simply:

```bash
kubectl delete deployment fastapi-deployment
kubectl delete service fastapi-service
```