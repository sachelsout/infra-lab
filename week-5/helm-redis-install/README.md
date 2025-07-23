# 📁 Day 29 — Helm Basics: Deploying Redis on Kubernetes

This day's focus was to understand Helm, a package manager for Kubernetes, and use it to deploy Redis on a local Kubernetes cluster via Docker Desktop.

## ✅ What We Did

### 🧰 Setup

- Platform: Kubernetes via Docker Desktop on Windows

- Shell Used: Git Bash (no WSL)

- Helm Installation:

    - Installed Helm from https://helm.sh

    - Verified installation using:

        ```bash
        helm version
        ```

### 📦 Installed Redis via Helm

1. Add Bitnami Helm chart repo:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

2. Install Redis with a release name (`redis-release`):

```bash
helm install redis-release bitnami/redis
```

3. Check pods and services:

```bash
kubectl get pods
kubectl get svc
```

### 🧪 Connect to Redis Pod and Verify

1. Forward the port to access Redis:

```bash
kubectl port-forward svc/redis-release-master 6379:6379
```

2. Open an interactive Redis shell inside the pod:

```bash
kubectl exec -it <redis-pod-name> -- redis-cli
```

Replace `<redis-pod-name>` with the actual pod, e.g., `my-redis-master-xxxxxxxxxx-yyyyy`

3. Run test commands:

```bash
PING
SET hello world
GET hello
```

Output:

```bash
PONG
"world"
```

## 🧹 Uninstalling Redis

To clean up:

```bash
helm uninstall redis-release
```

## ✅ Outcome

- Understood Helm commands: install, repo add, uninstall, upgrade

- Successfully deployed and tested Redis using Helm

- Ready to use Helm for templating our own applications

## 📁 Folder Name

```bash
helm-redis-setup/
```

Note: All Redis-related files were managed via Helm; no manual YAML files were created for Redis on this day.