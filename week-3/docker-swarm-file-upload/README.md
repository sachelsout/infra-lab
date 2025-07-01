# 📁 Docker Swarm File Upload App

A simple Flask-based file upload web app, containerized with Docker and deployed using Docker Swarm.

---

## 🚀 Features

- 📤 Upload and serve files via a web form.
- 🐳 Fully Dockerized and ready for Swarm.
- 💾 Persistent file storage using Docker volumes.
- ⚖️ Easily scalable via Swarm `replicas`.

---

## 📦 Tech Stack

- 🐍 Python 3.10 + Flask
- 🐳 Docker + Docker Swarm

---

## 📂 Folder Structure

```bash
docker-swarm-file-upload/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docker-stack.yml
└── README.md
```


> **Note**: Uploaded files are stored in a Docker-managed volume (`uploaded_data`), not in the local `uploads/` folder.

---

## 🐳 Important: Swarm Doesn't Support `build:` in YAML

Unlike Docker Compose, **Docker Swarm does NOT support building images from the `build:` directive** in your `docker-stack.yml`.

If you try to deploy a stack using `build:`, you'll see this error:

failed to create service fileupload_file-upload: Error response from daemon: rpc error: code = InvalidArgument desc = ContainerSpec: image reference must be provided


### ✅ Fix: Build and Push the Image Manually

1. **Build your Docker image locally** (from the `app/` directory):

```bash
docker build -t <your-dockerhub-username>/file-upload-app:latest ./app
```

2. **Push the image to Docker Hub**:
```bash
docker push <your-dockerhub-username>/file-upload-app:latest
```

3. **Update ```docker-stack.yml```**
Make sure your ```file-upload``` service uses the ```image:``` directive instead of ```build:```:

```yaml
services:
  file-upload:
    image: <your-dockerhub-username>/file-upload-app:latest
    ports:
      - "8000:8000"
    volumes:
      - uploaded_data:/uploads
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
```
Now you're ready to deploy:
```bash
docker stack deploy -c docker-stack.yml fileupload
```

#### ✅ Why this matters:
Swarm needs a pre-built image it can pull from a registry like Docker Hub — it doesn't build images during deployment like Compose does.

---

## 🛠️ Running the App

### 1. Clone the repo

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/week-3/docker-swarm-file-upload
```

### 2. Initialize Docker Swarm (only once)

```bash
docker swarm init
```

### 3. Deploy the stack

```bash
docker stack deploy -c docker-stack.yml fileupload
```

### 4. Access the app

Open your browser and go to: 📍 http://localhost:8000


## 📤 Uploaded Files

- Uploaded files are stored inside the Docker volume named uploaded_data.

- Files persist even after containers are restarted.


## 🧼 Teardown

To stop and remove the app and all related services:

```bash
docker stack rm fileupload
```