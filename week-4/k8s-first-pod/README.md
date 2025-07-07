# Day 22 – First Kubernetes Pod

## 📦 Project Structure

```plaintext
k8s-first-pod/
├── pod.yaml
├── README.md
```

---

## 🚀 Goal

Deploy a single NGINX container in Kubernetes using Docker Desktop's built-in K8s cluster.

---

## 🛠️ Steps

### 1. Apply the Pod manifest
```bash
kubectl apply -f pod.yaml
```

### 2. Verify it's running
```bash
kubectl get pods
kubectl describe pod hello-pod
```

### 3. Access NGINX in browser
```bash
kubectl port-forward pod/hello-pod 8080:80
```
Visit http://localhost:8080

---

## 🧼 Cleanup

```bash
kubectl delete pod hello-pod
```