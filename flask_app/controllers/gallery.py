from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for, session
from flask_app import app
from flask_app.models.file_model import File
from flask_app.models.user_model import User

@app.route("/my-gallery")
def gallery_view():
    user_id = session["user_id"]
    images = File.get_all(user_id)
    return render_template("gallery/view.html", images=images)

@app.route("/public_gallery")
def public_gallery():
    if "user_id" not in session:
        return redirect("/")
    
    user = User.get_by_id({"id": session["user_id"]})
    images = File.get_everything()
    return render_template("public_gallery.html", user=user, images=images, )
