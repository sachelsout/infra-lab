# 📁 Static File Server – Flask + Docker

This project demonstrates a simple **Flask-based static file server**, built with Docker and Docker Compose. It serves static files (like images and CSS) and HTML templates using bind mounts, making it easy to update without rebuilding the container.

---

## 📌 Features

- 🧠 **Flask app** to serve static files and HTML
- 🖼️ **Static folder** to serve CSS and image assets
- ⚙️ **Dockerized app** using `Dockerfile` and `docker-compose.yml`
- 📦 **Bind mounts** for real-time development — no need to rebuild!
- 📁 Clean project structure with separate folders for static & templates
- 🔄 Changes to `style.css` and `index.html` reflect immediately

---

## 🚀 Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/sachelsout/static-file-server
cd static-file-server
```
### 2. Set Up ```.env``` File
Create a ```.env``` file with the following:
```env
FLASK_ENV=development
```

### 3. Build and Run with Docker Compose
```bash
docker-compose up --build
```
Then visit: http://localhost:5000

## 🧪 Testing
- ✔️ Modify style.css and reload the browser – changes apply live.

- ✔️ Modify index.html and reload the browser – works instantly.

- ❌ Since we used bind mounts, using docker-compose down -v will not remove your static or template files (they’re on the host machine).

- 🧼 To clear files from uploads (if implemented), use rm commands on the static/uploads/ directory manually.

## 📂 Folder Structure

```arduino
.
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── image.jpg
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

## 🛠️ Tech Stack
- Python 3.x

- Flask

- Docker

- Docker Compose

## 📦 Docker Volumes Note
This app uses bind mounts:
```yaml
volumes:
  - ./static:/app/static
  - ./templates:/app/templates
```

#### This means even if you run ```docker-compose down -v```, your files are safe on the host. This setup is ideal for local development where you want live updates without rebuilding.