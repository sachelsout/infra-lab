from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/readyz")
def readiness_check():
    return {"ready": True}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb+") as f:
        f.write(await file.read())
    return {"info": f"file '{file.filename}' saved"}

@app.get("/files")
def list_files():
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}
