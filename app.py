from flask import Flask, render_template, request, redirect, url_for
from deepface import DeepFace
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Ensure 'uploads' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Clear the uploaded files before starting the app
def clear_files():
    try:
        files = os.listdir(app.config["UPLOAD_FOLDER"])
        for file in files:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file)
            os.remove(file_path)
    except Exception as e:
        print("An error occurred while clearing data:", e)

clear_files()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        if "file1" not in request.files or "file2" not in request.files:
            error = "Please provide two image files."
        else:
            file1 = request.files["file1"]
            file2 = request.files["file2"]

            if file1.filename == "" or file2.filename == "":
                error = "Please select two image files."
            elif not allowed_file(file1.filename) or not allowed_file(file2.filename):
                error = "Invalid file format. Only JPG, JPEG, and PNG files are allowed."
            else:
                file1_path = os.path.join(app.config["UPLOAD_FOLDER"], file1.filename)
                file2_path = os.path.join(app.config["UPLOAD_FOLDER"], file2.filename)
                file1.save(file1_path)
                file2.save(file2_path)
                try:
                    result = DeepFace.verify(file1_path, file2_path)
                except Exception as e:
                    error = "An error occurred during comparison. Please try again."
                    print(e)
                    if os.path.exists(file1_path):
                        os.remove(file1_path)
                    if os.path.exists(file2_path):
                        os.remove(file2_path)
                finally:
                    if os.path.exists(file1_path):
                        os.remove(file1_path)
                    if os.path.exists(file2_path):
                        os.remove(file2_path)
    return render_template("index.html", result=result, error=error)


@app.route("/clear", methods=["POST"])
def clear():
    clear_files()
    return redirect(url_for("index"))  # Redirect back to the index page after clearing

if __name__ == "__main__":
    app.run()
