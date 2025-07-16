# app/main.py

from fastapi import FastAPI
from pathlib import Path

app = FastAPI()
data_file = Path("/data/notes.txt")

@app.post("/write")
def write_note(note: str):
    data_file.parent.mkdir(parents=True, exist_ok=True)
    with open(data_file, "a") as f:
        f.write(note + "\n")
    return {"message": "Note written!"}

@app.get("/read")
def read_notes():
    if not data_file.exists():
        return {"notes": []}
    with open(data_file, "r") as f:
        return {"notes": f.read().splitlines()}
