# 🐳 Docker Compose + Flask + Redis App (A Day 3 Infra Project)

This project demonstrates a simple counter web app using Flask and Redis, containerized using Docker Compose.

## 📦 Tech Stack

- Python + Flask
- Redis (as a service)
- Docker & Docker Compose
- `.env` support via `python-dotenv`

---

## ⚙️ Project Structure

```plaintext
flask-redis-compose-app/
├── app.py                  # Flask app
├── Dockerfile              # Image for web app
├── docker-compose.yml      # Multi-container config
├── requirements.txt        # Python dependencies
├── .env                    # Config variables (Redis host/port)
└── static/
    └── favicon.ico         # Optional browser icon
```


---

## 🚀 How to Run

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/flask-redis-compose-app

# Build and run
docker compose up --build
```

## 🌐 Access the App
Visit http://localhost:5000

Each page refresh increments the counter stored in Redis.

## 🧪 Environment Variables
Defined in `.env`:
```
FLASK_ENV=development
REDIS_HOST=redis
REDIS_PORT=6379
```
These are loaded into the Flask app using `python-dotenv`.

## 🛠️ Stopping the App
```
docker compose down
```