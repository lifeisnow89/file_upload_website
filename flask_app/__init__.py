from flask import Flask
from flask_bcrypt import Bcrypt
import os
from newsapi.newsapi_client import NewsApiClient

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "shhhhhh"

app.config["UPLOAD_DIR"] = os.path.join(app.instance_path, "uploads")
os.makedirs(app.config["UPLOAD_DIR"], exist_ok=True)