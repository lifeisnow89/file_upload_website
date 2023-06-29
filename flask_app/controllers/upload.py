import os
from flask import Flask, flash, render_template,redirect,request,session, send_from_directory
from flask_app import app
from flask_app.models.file_model import File
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
import uuid
from flask_app.utils import save_profile_pic, delete_profile_pic, save_gallery_image
bcrypt = Bcrypt(app)

@app.route("/upload")
def upload_file():
    return render_template("uploads/upload_file.html")

@app.route("/uploads/<filename>")
def serve_files(filename):
    return send_from_directory(app.config["UPLOAD_DIR"], filename)

@app.route("/set-profile-pic")
def show_form():
    if "user_id" not in session:
        return redirect("/")
    
    user = User.get_by_id({"id": session["user_id"]})
    return render_template("uploads/set-profile-pic.html", user=user)

@app.route("/set-profile-pic", methods=['POST'])
def store_profile_pic():
    file = request.files["my_file"]
    save_profile_pic(file, session["user_id"])
    print(app.config["UPLOAD_DIR"])
    flash("Profile pic updated", "success")
    return redirect("/set-profile-pic")

@app.route("/delete-profile-pic", methods=["POST"])
def delete_profile_pic_form():
    delete_profile_pic(session["user_id"])
    flash("Profile pic deleted", "success")
    return redirect("/set-profile-pic")

@app.route("/gallery/view", methods=["POST"])
def store_image():
    file = request.files["my_file"]
    save_gallery_image(file, session["user_id"])
    flash("Gallery image has been uploaded!", "success")
    return render_template("/upload.html")


# @app.route("/upload", methods=["POST"])
# def file_upload():
#     if "my_file" not in request.files:
#         error_response = {
#             "error": "File does not exist",
#         }
#         return error_response
    
#     my_file = request.files["my_file"]

#     unique_filename = save_uploaded_file(my_file, session["user_id"])

#     flash("File upload successful", "success")
#     return redirect("/upload")