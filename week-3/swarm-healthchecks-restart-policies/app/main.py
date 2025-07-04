from fastapi import FastAPI, Response, status
import time
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Docker Swarm!"}

@app.get("/health")
def health_check(response: Response):
    if random.random() < 0.8:
        return {"status": "healthy"}
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": "unhealthy"}
