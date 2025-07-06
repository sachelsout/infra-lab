# 📝 FastAPI Blog App (Docker Swarm Edition)

A simple blog backend built with **FastAPI** and **PostgreSQL**, containerized using **Docker**, and deployed using **Docker Swarm**. This app supports creating, reading, updating, and deleting blog posts.

---

## 📦 Features

- RESTful API using FastAPI
- PostgreSQL as the database
- SQLAlchemy ORM
- Dockerized for production use
- Deployed using Docker Swarm
- Persistent data using named volumes

---

## 📁 Folder Structure

```plaintext
swarm-app-with-db/
├── app/
│ ├── main.py
| ├── database.py
| ├── models.py
│ ├── requirements.txt
│ └── Dockerfile
├── db/
│ └── init.sql # (Optional) Initial setup for Postgres
├── secrets/
│ └── db_password.txt # Docker Swarm secret (Postgres password)
├── configs/
│ └── app_config.env # Docker Swarm config (environment variables)
├── docker-stack.yml
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-3/swarm-app-with-db
```

### 2. Build and push the Docker image
Make sure you're logged into Docker Hub and replace rohan2304 with your Docker Hub username if needed.
```bash
docker build -t rohan2304/blog-fastapi:latest ./app
docker push rohan2304/blog-fastapi:latest
```

### 3. Initialize Docker Swarm (if not already)

```bash
docker swarm init
```

### 4. Deploy the stack

```bash
docker stack deploy -c docker-stack.yml blogapp
```
🐳 This will spin up the FastAPI app and PostgreSQL service using secrets, configs, and a persistent volume for the database.

---

## 🌐 Access the API
Open your browser or API tool (e.g., Postman, Hoppscotch):
```bash
http://localhost:8000/posts
```

---

## 🚀 API Endpoints

| Method | Endpoint           | Description                  |
|--------|--------------------|------------------------------|
| GET    | `/posts`           | Get all blog posts           |
| GET    | `/posts/{post_id}` | Get a single post by ID      |
| POST   | `/posts`           | Create a new post            |
| PUT    | `/posts/{post_id}` | Update an existing post      |
| DELETE | `/posts/{post_id}` | Delete a post by ID          |

---

## 🧹 How to Clean Up
To remove the Docker stack:

```bash
docker stack rm blogapp
```

To remove the volume (⚠️ this deletes all Postgres data):

```bash
docker volume rm blogapp_postgres_data
```

To remove all unused Docker resources (images, containers, volumes):

```bash
docker system prune -af --volumes
```