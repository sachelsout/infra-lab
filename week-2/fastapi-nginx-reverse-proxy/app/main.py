from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI behind Nginx"}

@app.get("/health")
def health():
    return {"status": "ok"}
