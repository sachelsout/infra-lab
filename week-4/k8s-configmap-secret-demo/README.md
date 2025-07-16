# 📦 Day 24 – Kubernetes ConfigMaps and Secrets with FastAPI

This project demonstrates how to use ConfigMaps and Secrets in Kubernetes to inject configuration and sensitive data (like passwords or API keys) into a FastAPI application.

## 📁 Folder Structure

```plaintext
k8s-configmap-secret-demo/
├── app/
│   └── main.py
├── configmap.yaml
├── secret.yaml
├── deployment.yaml
├── services.yaml
└── Dockerfile
```

## 🚀 What We Did

- Created a basic FastAPI app that reads:

    - A welcome message from a `ConfigMap`

    - A fake database password from a `Secret`

- Deployed this app to Kubernetes using `kubectl apply`.

- Verified the environment variables were injected correctly using `localhost:<PORT>` in the browser.

## ⚙️ Setup Instructions

1. Start Kubernetes <br>

Ensure Kubernetes is enabled in Docker Desktop or use Minikube.

2. Clone the Repo

```bash
git clone https://github.com/rohan2304/infra-lab.git
cd infra-lab/week-4/k8s-configmap-secret-demo/
```

3. Create ConfigMap and Secret

```bash
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
```

4. Deploy the FastAPI App

```bash
kubectl apply -f deployment.yaml
```

5. Expose the App via Service

```bash
kubectl apply -f services.yaml
```

6. Access the App

Visit the app in your browser:

```arduino
http://localhost:<PORT>
```

You should see a response like:

```json
{
  "message": "Welcome to Kubernetes!",
  "db_password": "super-secret-password"
}
```

## 🧼 Cleanup

To delete all Kubernetes resources created:

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
kubectl delete -f configmap.yaml
kubectl delete -f secret.yaml
```