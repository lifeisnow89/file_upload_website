from flask import Flask, flash, render_template,redirect,request,session
from flask_app import app
from flask_app.models.file_model import File
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

print("connected!!!!!!!!!!!!!!!!!!!!!!!!")

@app.route('/')
def index():
    return render_template('login_reg.html')


@app.route("/register", methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "email": request.form['email'],
        "username": request.form['username'],
        "password": pw_hash,

    }
    user = User.get_by_email(data)
    id = User.save(data)
    session['user_id'] = id
    return redirect("/dashboard")

@app.route("/login",methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    session['username'] = user.username
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():    
    return render_template("/dashboard.html")

@app.route('/upload')
def upload():    
    return render_template("/upload.html")

@app.route('/news')
def news():    
    return render_template("/news.html")

# @app.route("/public_gallery")
# def public_gallery():
#     if "user_id" not in session:
#         return redirect("/")
    
#     user = User.get_by_id({"id": session["user_id"]})
#     images = File.get_everything()
#     return render_template("public_gallery.html", user=user)
