from flask import Flask
import os
import redis
from flask import send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('hits')
    return f'Hello! This page has been visited {count} times.'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)