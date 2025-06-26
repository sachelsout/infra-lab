# 📦 CI/CD with GitHub Actions — Docker Build & Push

This project demonstrates how to set up **Continuous Integration and Deployment (CI/CD)** for a Dockerized Flask app using **GitHub Actions**.

We use **GitHub Container Registry (GHCR)** to push the Docker image automatically whenever a change is pushed to the `main` branch.

---

## 🚀 What This Project Does

- Builds a Docker image from a Flask file-upload app
- Pushes the image to **GitHub Container Registry (GHCR)**
- Automates everything with GitHub Actions on `git push` or pull requests to `main`

---

## 🧱 Project Structure

```android
infra-lab/
├── file-upload-app/
│ ├── app.py
│ ├── requirements.txt
│ ├── Dockerfile
│ ├── ...
│
└── .github/
    └── workflows/
        └── docker.yml <-- CI/CD workflow file
```


---

## ⚙️ GitHub Actions Workflow

Located in: `.github/workflows/docker.yml`

### ✅ Triggered On:
- Push to `main` branch (only if changes in `file-upload-app/` or workflow file)
- Pull requests to `main`

### 🛠️ What It Does:

1. **Checks out the code**
2. **Sets up Docker Buildx**
3. **Authenticates to GHCR**
4. **Builds and pushes Docker image to** `ghcr.io/<your-username>/file-upload-app:latest`

---

## 🔐 Secrets & Permissions

Make sure the following are correctly configured:

- In `docker.yml`:
  ```yaml
  permissions:
    contents: read
    packages: write

#### No additional secrets are needed — GITHUB_TOKEN handles GHCR authentication.

## 🐳 Docker Image

- Image pushed to:<br>
```ghcr.io/<your-username>/file-upload-app:latest```

You can view it under your Packages tab on GitHub

## 📝 Notes

- Uses bind mounts for file persistence in the Flask app

- You can easily extend this to deploy the container using services like:

    - AWS ECS

    - Railway

    - Render

    - Fly.io

## 📂 Folder Location
This CI/CD setup applies to the folder: ```file-upload-app/```

## ✅ Outcome

Every time you push changes to ```main```:

- The Docker image is built from the latest source

- It’s pushed to GHCR without any manual intervention

## 📸 Screenshots

[![Build and Push Docker Image](https://github.com/sachelsout/infra-lab/actions/workflows/docker.yml/badge.svg)](https://github.com/sachelsout/infra-lab/actions/workflows/docker.yml)

## 📚 Learning Outcomes

- GitHub Actions workflows

- Docker Buildx and caching

- Auth to GHCR using GITHUB_TOKEN

- Modular folder-based CI/CD targeting