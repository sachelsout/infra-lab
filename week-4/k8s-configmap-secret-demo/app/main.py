from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/config")
def read_config():
    message = os.getenv("WELCOME_MESSAGE", "Default message")
    return {"message": message}

@app.get("/secret")
def read_secret():
    db_user = os.getenv("DB_USER", "user not set")
    db_pass = os.getenv("DB_PASS", "password not set")
    return {"db_user": db_user, "db_pass": db_pass}
