from flask import Flask, request, jsonify, render_template
import psycopg2
import os

app = Flask(__name__)

# Database connection parameters from environment
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_USER = os.getenv("POSTGRES_USER", "myuser")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "mypassword")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_name():
    name = request.form.get("name") or request.json.get("name")
    if not name:
        return jsonify({"error": "No name provided"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO people (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": f"Added {name} successfully!"})

@app.route("/list", methods=["GET"])
def list_names():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM people")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# Initialize DB table before app starts
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
