# Dockerized Flask ML App – A Day 2 Infra Project 🚀

## 🧠 What I Built
A machine learning model (Logistic Regression on Iris dataset) exposed via a Flask API and containerized using Docker. This taught me how to serve ML models inside reproducible containers.

## 🛠 Tech Stack
- Python + Flask
- Scikit-learn
- Docker

## 📦 How to Run

```bash
git clone https://github.com/sachelsout/infra-lab.git
cd infra-lab/flask-ml-docker-app

# Train the model and generate model.pkl
python train.py

# Build Docker image
docker build -t flask-ml-docker-app .

# Run container
docker run -p 5000:5000 flask-ml-docker-app
```

Then go to: http://localhost:5000/predict

## 🧪 Sample Test (with curl/Postman)

Send a POST request to:

```bash
http://localhost:5000/predict
```

With this JSON body:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Expected response:

```json
{
  "prediction": "setosa"
}
```

## ✅ Ways to test:
#### Using curl:

```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

#### Or use Postman to send a POST request with the above JSON to
http://localhost:5000/predict