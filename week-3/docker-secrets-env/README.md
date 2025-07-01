# 🔐 Docker Swarm - Secrets & Environment Variables (Day 16)

This project demonstrates how to **securely manage secrets and configuration** in a production-ready Flask application using **Docker Swarm**.

---

## 📎 GitHub Clone & Run
```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-3/docker-secrets-env
```

---

## 📦 Folder Structure

```bash
docker-secrets-env/
├── app/
│   ├── main.py         # Flask app that reads secret & config
│   ├── requirements.txt
│   └── Dockerfile
├── secrets/
│   └── api_key.txt     # Secret key used by the app
├── docker-stack.yml    # Docker Swarm stack definition
└── README.md
```

---

## 🔧 What This Project Does

- Uses **Docker Swarm secrets** for sensitive data like passwords.
- Uses **Docker Swarm configs** for general configuration (non-sensitive).
- Mounts secrets and configs inside the container as **read-only files**.
- Demonstrates how to read secrets and configs from a Flask app.

---

## 🐋 Run Instructions

### 1. Initialize Docker Swarm (if not already)
```bash
docker swarm init
```

### 2. Create a Docker secret from file
```bash
docker secret create api_key secret/api_key.txt
```

### 3. Build the image
```bash
docker build -t rohan2304/file-upload-app:secrets-env ./app
```

### 4. Deploy the stack
```bash
docker stack deploy -c docker-stack.yml secretstack
```

### 5. Visit the app
Open in browser: http://localhost:8000
You should see:
```json
{
  "api_key": "your-actual-secret-key"
}
```

## ✅ Why This Matters

- 🔒 No hardcoding sensitive keys.

- 🔐 Secrets are encrypted and isolated per service.

- 🛡️ Better than using environment variables directly for secret data.