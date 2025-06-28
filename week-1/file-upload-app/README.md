# 📁 File Upload App with Flask + Docker (Bind Mount)

This simple app demonstrates how to:

- Upload files via a web form using Flask
- Serve them back as downloadable links
- Persist uploaded files using a **bind mount**
- Run everything inside a Docker container

---

## 🧱 Tech Stack

- Python 3.10
- Flask
- Docker
- Bind mount for data persistence

---

## 📦 Folder Structure
```plaintext
file-upload-app/
├── app.py              # Flask web app
├── templates/
│ └── index.html        # HTML form for upload
├── uploads/            # Uploaded files (bind mounted)
├── Dockerfile          # Image build for Flask app
├── .env                # Environment variables
└── docker-compose.yml  # Service config
```


---

## 🚀 How to Run

1. Build and start the container:
```bash
docker-compose up --build
```
2. Open your browser at:
```bash
http://localhost:5000
```
3. Upload files using the form. They will be saved to the uploads/ folder and served as downloadable links.

## 💾 Data Persistence (Bind Mount)
Uploaded files are saved on your host machine via a bind mount:
```bash
volumes:
  - ./uploads:/app/uploads
```

This means:
- Uploaded files persist even if the container is stopped or deleted.

- This is not a Docker-managed volume, so running:
```bash
docker-compose down -v
```
will NOT remove the uploaded files.

## 🧹 How to Delete Uploaded Files
To delete uploaded files:

### 🔸 Option 1: Manual deletion from host
```bash
rm -rf uploads/*
```

### 🔸 Option 2: (Optional) Dev-only cleanup route in Flask
If you added this route in app.py:
```python
@app.route('/clear', methods=['POST'])
def clear_uploads():
    folder = app.config['UPLOAD_FOLDER']
    for filename in os.listdir(folder):
        os.remove(os.path.join(folder, filename))
    return "Uploads cleared!"
```

Then send a POST request to /clear:
```bash
curl -X POST http://localhost:5000/clear
```