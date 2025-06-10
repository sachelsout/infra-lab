# 🚀 Dockerizing My First Python Flask App – A Day 1 Infra Project

## 🧱 What I Built

A simple Flask web app containerized using Docker.

The goal was to:
- Understand Docker images & containers
- Write a basic Dockerfile
- Run a service locally in an isolated, reproducible way

---

## 🔧 Tech Stack

- Python + Flask  
- Docker  
- Git & GitHub  

---

## 📦 How to Run

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/flask-docker-app
docker build -t flask-docker-app .
docker run -p 5000:5000 flask-docker-app


Then visit 👉 http://localhost:5000