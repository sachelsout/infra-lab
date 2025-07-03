# 📦 Day 17 - Docker Swarm Multi-Host App with Overlay Networking

This project demonstrates deploying a FastAPI + Redis application using **Docker Swarm** with **overlay networking**, enabling services to communicate across multiple Docker nodes.

---

## 🧠 What You’ll Learn

- How to initialize and use Docker Swarm
- How to create overlay networks for multi-host communication
- How to deploy and manage services in a stack
- How service discovery works using Docker DNS

---

## 🗂️ Project Structure

```plaintext
docker-swarm-multihost/
├── app/
│ ├── main.py
│ ├── Dockerfile
│ └── requirements.txt
│
└── docker-stack.yml
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-3/docker-swarm-multihost
```

### 2. Build and Push the App Image

```bash
docker build -t rohan2304/file-upload-app:latest ./app
docker push rohan2304/file-upload-app:latest
```

### 3. Initialize Docker Swarm (if not already done)

```bash
docker swarm init
```

### 4. Deploy the Stack

```bash
docker stack deploy -c docker-stack.yml multi-host
```

### 5. Access the App
Visit http://localhost:8000

---

## 🧩 docker-stack.yml

```yaml
version: '3.8'

services:
  app:
    image: rohan2304/multi-host-app:latest
    build: ./app
    ports:
      - "8000:8000"
    networks:
      - overlay-net

  redis:
    image: redis:alpine
    networks:
      - overlay-net

networks:
  overlay-net:
    driver: overlay
```

## 📊 What’s Happening

- A FastAPI app connects to Redis using Docker Swarm’s built-in DNS (redis).

- Both services share an overlay network, allowing cross-node communication.

- Swarm manages availability and communication automatically.

## 🧼 Cleanup

```bash
docker stack rm multi-host
```