# Postgres + Flask Dockerized App

This is a simple web application built with Flask and PostgreSQL, containerized using Docker Compose. It demonstrates:

- Web form submission using Flask
- PostgreSQL integration
- Docker volumes for database persistence
- Environment-based configuration

---

## 🏗️ Project Structure

```plaintext
postgres-flask-app/
├── app.py              # Flask application
├── Dockerfile          # Image for Flask app
├── docker-compose.yml  # Multi-container config
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
└── templates/
    └── index.html      # HTML form
```

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/postgres-flask-app
```

### 2. Start the containers
```bash
docker-compose up --build
```

Visit: http://localhost:5000

## ✅ Features
- Submit names using a web form.

- All submitted names are stored in a PostgreSQL database.

- Submitted data persists even after restarting containers.

## 💾 Data Persistence
We use Docker volumes to persist PostgreSQL data.

Even after stopping and removing containers with:
```bash
docker-compose down
```
...the data still remains

To delete containers + volumes (and wipe all data):
```bash
docker-compose down -v
```

## ⚙️ Environment Variables
Stored in .env file:
```bash
POSTGRES_DB=mydb
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_HOST=db
```
Flask reads these via `os.getenv(...)` calls in `app.py`.

## 📥 Example Entry
1. Enter a name in the form (e.g., Rohan)

2. Hit submit

3. Name is saved in PostgreSQL and shown on the homepage

## 📚 Commands

- View logs: ```docker-compose logs```

- Rebuild containers: ```docker-compose up --build```

- Stop: ```docker-compose down```

- Wipe everything: ```docker-compose down -v```