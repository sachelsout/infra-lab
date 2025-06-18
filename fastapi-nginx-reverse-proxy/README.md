# Day 8: Nginx as a Reverse Proxy + Healthchecks (FastAPI)

This project demonstrates how to use **Nginx as a reverse proxy** to serve a **FastAPI application**. It also includes a simple healthcheck setup to ensure the app is up and running.

---

## 📌 Project Structure

```arduino
day08-nginx-reverse-proxy/
├── app/
│ └── main.py               # FastAPI application
│ └── Dockerfile            # FastAPI Dockerfile
│ └── requirements.txt      # requirements file
├── nginx/
│ └── default.conf          # Nginx reverse proxy configuration             
├── docker-compose.yml      # Orchestrates FastAPI and Nginx services
```
---

## 🚀 What This Project Does

✅ Runs a **FastAPI** web server  
✅ Uses **Nginx** as a reverse proxy to route external traffic to FastAPI  
✅ Implements a `/health` endpoint for **Docker healthcheck**  
✅ Dockerized using **Docker Compose**

---

## 📦 Technologies Used

- FastAPI (Python)
- Uvicorn ASGI server
- Nginx (as reverse proxy)
- Docker
- Docker Compose

---

## 🛠️ How to Run

```bash
# Clone the repo from the repository
git clone https://github.com/sachelsout/fastapi-nginx-reverse-proxy

# cd to root directory
cd fastapi-nginx-reverse-proxy

# From project root directory
docker-compose up --build
```
Then visit: http://localhost:8080

## 📎 Endpoints
| Endpoint  | Description                               |
| --------- | ----------------------------------------- |
| `/`       | Returns "Hello from FastAPI behind Nginx" |
| `/health` | Used for Docker healthcheck               |

## 💡 Why Use a Reverse Proxy?
- Separation of concerns: Nginx handles routing, caching, and SSL while FastAPI focuses on app logic

- Scalability: Easily load balance across multiple app instances

- Security: Hides internal app architecture

- Performance: Caching and connection pooling

## ⚠️ Notes
- The FastAPI app runs on port 8000 internally

- Nginx listens on port 8080 and forwards traffic to FastAPI

- Logs for both containers are visible using docker-compose logs

## 📚 Learning Outcome
This project taught how to:

- Use Nginx as a reverse proxy

- Serve a FastAPI app through Nginx

- Configure Docker healthchecks

- Build a production-ready service layer