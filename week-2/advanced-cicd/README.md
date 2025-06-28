# 🚀 Advanced CI/CD with GitHub Actions – Day 12

[![Test, Build and Push Docker Image](https://github.com/sachelsout/infra-lab/actions/workflows/docker.yml/badge.svg)](https://github.com/sachelsout/infra-lab/actions/workflows/docker.yml)

This project enhances the CI/CD pipeline of the existing **file-upload-app** by introducing:

- ✅ Automated testing with `pytest`
- 🐳 Building and pushing Docker images to **GitHub Container Registry (GHCR)**
- 🔁 Workflow triggers for `push` and `pull_request` events
- 📁 Context-aware build paths for monorepos

---

## 📁 Folder Structure

```bash
infra-lab/
├── week-1/
│   ├── file-upload-app/
│     ├── app.py
│     ├── Dockerfile
│     ├── requirements.txt
│     ├── test_app.py
│     ├── uploads/
│     └── ...
├── .github/
│   └── workflows/
│       └── docker.yml
```

## ⚙️ GitHub Actions Workflow (docker.yml)

```yml
name: Test, Build and Push Docker Image

on:
  push:
    branches: [ main ]
    paths:
      - 'week-1/file-upload-app/**'
      - '.github/workflows/docker.yml'
  pull_request:
    branches: [ main ]
    paths:
      - 'week-1/file-upload-app/**'
      - '.github/workflows/docker.yml'
permissions:
      contents: read
      packages: write
jobs:
  test-and-build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
      
    - name: Install dependencies
      working-directory: ./week-1/file-upload-app
      run: |
        pip install -r requirements.txt

    - name: Run tests
      working-directory: ./week-1/file-upload-app
      run: |
        pytest

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3

    - name: Log in to GitHub Container Registry
      uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v5
      with:
        context: ./week-1/file-upload-app
        push: true
        tags: ghcr.io/sachelsout/file-upload-app:latest
```

## 🧪 Testing with pytest
- A sample test (test_app.py) is added to verify if the Flask app initializes properly.

- To run tests locally:

```bash
cd week-1/file-upload-app
pytest
```

## 🐳 Docker Image

After a successful workflow run, your image is pushed to:

```bash
ghcr.io/sachelsout/file-upload-app:latest
```

#### Make sure your repo has GitHub Packages access enabled.

## 📌 Notes

- Ensure the /uploads directory exists with correct write permissions.

- Use .dockerignore to prevent unnecessary files from bloating your image.

- Keep secrets like GITHUB_TOKEN secure via GitHub’s secrets UI.