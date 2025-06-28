from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["DEBUG"] = True

# Serve static files from 'static' folder
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
