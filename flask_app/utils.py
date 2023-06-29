import os
import uuid
from flask_app import app
from flask_app.models.file_model import File
from flask_app.models.user_model import User

def save_profile_pic(file, user_id):
    file_extension = os.path.splitext(file.filename)[1]
    unique_string = uuid.uuid4().hex
    file_fullname = unique_string + file_extension
    file.save(os.path.join(app.config["UPLOAD_DIR"], file_fullname))
    User.set_profile_pic({
        "user_id": user_id, 
        "profile_pic": file_fullname
    })
    return True

def delete_profile_pic(user_id):
    user = User.get_by_id({"id": user_id})
    if not user.profile_pic:
        return False
    file_path = os.path.join(app.config["UPLOAD_DIR"], user.profile_pic)
    if os.path.exists(file_path):
        os.remove(file_path)
    User.set_profile_pic({
        "user_id": user_id,
        "profile_pic": ""
    })
    return True

def save_gallery_image(file, user_id):
    file_extension = os.path.splitext(file.filename)[1]
    unique_string = uuid.uuid4().hex
    file_name = unique_string + file_extension
    file_new_path = os.path.join(app.config["UPLOAD_DIR"], file_name) #/var/our_app/instance/uploads/wagajdfagdfagsd.png
    file.save(file_new_path)
    File.save({
        "file_name": file_name,
        "extension": file_extension,
        "size": os.stat(file_new_path).st_size,
        "user_id": user_id,
    })
    return True