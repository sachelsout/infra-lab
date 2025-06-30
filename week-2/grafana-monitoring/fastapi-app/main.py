from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter("app_requests_total", "Total number of requests to this API")

@app.get("/")
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello, Grafana + Prometheus!"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
