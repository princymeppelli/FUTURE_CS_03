from flask import (
    Flask, render_template, request,
    send_file, session, redirect, url_for
)
import os
import io
from flask import flash
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)

# Secret key for Flask session
app.secret_key = "simple_secret_key_for_demo"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# 🔐 Load persistent AES key (IMPORTANT)
with open("secret.key", "rb") as key_file:
    AES_KEY = key_file.read()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- UPLOAD (PUBLIC) ----------------
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    if not file:
        return {"status": "error", "message": "No file selected"}

    file_data = file.read()

    iv = get_random_bytes(16)
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))

    encrypted_file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename + ".enc"
    )

    with open(encrypted_file_path, "wb") as f:
        f.write(iv + encrypted_data)

    return {"status": "success", "message": "File uploaded successfully 🔐"}


# ---------------- FILE LIST ----------------
@app.route("/files")
def list_files():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("files.html", files=files)


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":
            session["logged_in"] = True
            flash("success")
            return redirect(session.get("next_url", "/files"))
        else:
            flash("unauthorized")

    return render_template("login.html")



# ---------------- DOWNLOAD (PROTECTED) ----------------
@app.route("/download/<filename>")
def download_file(filename):

    # 🔐 Require login
    if not session.get("logged_in"):
        session["next_url"] = url_for("download_file", filename=filename)
        return redirect(url_for("login"))

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    with open(file_path, "rb") as f:
        file_data = f.read()

    iv = file_data[:16]
    encrypted_data = file_data[16:]

    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    original_filename = filename.replace(".enc", "")

    # 📥 Prepare download response
    response = send_file(
        io.BytesIO(decrypted_data),
        as_attachment=True,
        download_name=original_filename
    )

    # 🔒 SOLUTION-1: Logout AFTER download
    session.pop("logged_in", None)

    return response


# ---------------- LOGOUT (OPTIONAL) ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
