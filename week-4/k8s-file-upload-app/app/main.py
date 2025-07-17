from fastapi import FastAPI, UploadFile, File
import os
from typing import List

app = FastAPI()

UPLOAD_DIR = "/app/uploads"  # Absolute path
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"message": f"File '{file.filename}' uploaded successfully."}

@app.get("/files")
def list_files():
    files = os.listdir(UPLOAD_DIR)
    return {"uploaded_files": files}
