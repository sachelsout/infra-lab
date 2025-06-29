# 📦 Flask + Redis + Docker Volumes (Day 4 – Infra Lab)

This project demonstrates how to:
- Build a **Flask web app** connected to **Redis**
- Increment a **counter** with a user-defined **limit**
- Achieve **data persistence** using **Docker volumes**

Even if the container is stopped or removed, the Redis data (counter value) persists across sessions.

---

## 🗂️ Project Structure


```plaintext
flask-redis-volume-app/
├── app.py                  # Flask app
├── Dockerfile              # Image for web app
├── docker-compose.yml      # Multi-container config
├── requirements.txt        # Python dependencies
├── .env                    # Config variables (Redis host/port)
```


---

## 🚀 How to Run

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-1/flask-redis-volume-app

# Build and run
docker compose up --build
```

## 🌐 Access the App
Visit http://localhost:5000

## 🧪 Features
- 🧮 Counter: Increments every time the page is refreshed.

- 🎯 Limit: Set a max limit using the HTML form.

- ♻️ Persistence: Redis data is stored in a Docker volume, so the counter persists across container rebuilds.

## 🔧 Docker Volume
```
volumes:
  redis-data:
```
Redis is configured to store its database in this volume:
```
docker volume ls
docker volume inspect redis-data
```

## 🛡️ Important Note:
Even if you stop or delete the containers, the volume (redis-data) will remain intact and retain the counter value.

To delete the volume as well (⚠️ this will reset the counter):
```
docker compose down -v
```


## 🧱 Tech Stack
- Python 3.10

- Flask

- Redis

- Docker & Docker Compose

- HTML/Jinja2 templates

## 📬 Sample Interaction
1. Submit a number as the limit using the web form.

2. Refresh the page.

3. The counter increments until it hits the set limit.

## ✅ Example Output
If limit = 3, and the counter reaches 3:
```
Counter has reached the limit: 3
```