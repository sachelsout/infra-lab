# Day 28 – Kubernetes Dashboard Monitoring

On Day 28 of the Infrastructure Engineering journey, we explored how to set up and use the **Kubernetes Dashboard** to monitor the FastAPI app (`k8s-probes-demo`) we built on Day 27.

## 📌 Goal

- Deploy the Kubernetes Dashboard on our local cluster (Minikube or Docker Desktop).
- Create a service account with the necessary permissions.
- Access the dashboard securely.
- Use the dashboard to monitor the FastAPI app and understand key resource metrics.

---

## 🧱 Folder Structure

```plaintext
k8s-dashboard-monitoring/
├── dashboard-admin-user.yaml # RBAC setup for Dashboard access
```

> The FastAPI app (`k8s-probes-demo`) code is **not duplicated** here. We simply reused the app from **Day 27**.

---

## 🛠️ Step-by-Step Setup

### 1. ✅ Start Kubernetes Cluster

Make sure your Kubernetes cluster is running (Docker Desktop or Minikube):

```bash
kubectl config current-context
kubectl get nodes
```

### 2. 🚀 Deploy Kubernetes Dashboard

Apply the official dashboard manifest:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

### 3. 👤 Create Admin User

We used the provided ```dashboard-admin-user.yaml``` file:

```yaml
# dashboard-admin-user.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
```

Apply it:

```bash
kubectl apply -f dashboard-admin-user.yaml
```

### 5. 🌐 Access the Dashboard

Forward the dashboard service to your local machine:

```bash
kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8080:443
```

Now open your browser and go to:<br>
👉 http://localhost:8080

Use the token to log in.

## 📊 Monitoring the FastAPI App

We previously deployed our FastAPI app (```k8s-probes-demo```) on Day 27 using:

- Kubernetes Deployment + Service

- Readiness and Liveness probes

In the Dashboard:

- Go to Workloads > Deployments

- View pod health, logs, and probe status

- Go to Services to check service exposure

- Use Metrics (if available) to view CPU/memory usage

This gives a visual insight into how your app is behaving inside the cluster.

## 🧹 Cleanup

To delete the dashboard and admin user:

```bash
kubectl delete -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl delete -f dashboard-admin-user.yaml
```

Or delete all dashboard resources manually:

```bash
kubectl delete namespace kubernetes-dashboard
```

## ✅ Summary

- ✔️ Set up Kubernetes Dashboard.

- 🔐 Created admin access with service account + token.

- 📈 Monitored an existing FastAPI app from Day 27.

- 🧹 Cleaned up all resources after use.

### 📂 App being monitored: k8s-probes-demo/ (from Day 27)
### 🗂️ Dashboard setup files: k8s-dashboard-monitoring/