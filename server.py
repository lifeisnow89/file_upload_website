from flask_app import app
from flask_app.models import user_model
from flask_app.models import file_model
from flask_app.controllers import users
from flask_app.controllers import upload
from flask_app.controllers import gallery
from flask_app.controllers import news

if __name__=="__main__":
    app.run(debug=True)