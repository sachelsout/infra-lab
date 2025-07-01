from flask import Flask, request, send_from_directory
import os

UPLOAD_FOLDER = "/uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return '''
        <h1>Upload a File</h1>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <input type="file" name="file" />
            <input type="submit" value="Upload" />
        </form>
    '''

@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]
    if uploaded_file.filename != "":
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(filepath)
        return f"File uploaded successfully. <a href='/uploads/{uploaded_file.filename}'>Download</a>"
    return "No file uploaded."

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
