from flask import Flask
import os

app = Flask(__name__)

def read_secret(path="/run/secrets/api_key"):
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except Exception as e:
        return f"Error reading secret: {e}"

@app.route("/secret")
def get_secret():
    app_env = os.getenv("APP_ENV", "Not Set")
    api_key = read_secret()
    return {
        "environment": app_env,
        "api_key": api_key
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
