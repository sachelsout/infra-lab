from fastapi import FastAPI
import redis
import os

app = FastAPI()

# Redis hostname = service name from docker stack
r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    count = r.incr("hits")
    return {"message": f"This page has been viewed {count} times."}