from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import file_model
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

class User:
    db = 'files'
    def __init__(self, data):
        self.id = data['user_id']
        self.email = data['email']
        self.username = data['username']
        self.profile_pic = data['profile_pic']
        self.password = data['password']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (email, username, password) VALUES (%(email)s, %(username)s, %(password)s);"
        return connectToMySQL("graduation_project").query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('graduation_project').query_db(query)
        users = []
        for d in results:
            users.append( cls(d) )
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('graduation_project').query_db(query,data)
        if len(results) < 1:
            return False
        print (results[0])
        return cls(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE user_id = %(id)s;"
        results = connectToMySQL('graduation_project').query_db(query,data)
        if len(results) < 1:
            return False
        print (results[0])
        return cls(results[0])
    
    @classmethod
    def set_profile_pic(cls, data):
        query = "UPDATE users SET profile_pic=%(profile_pic)s WHERE user_id=%(user_id)s"
        results = connectToMySQL('graduation_project').query_db(query, data)
        return results

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['email']) >= 1:
            flash("Email already taken", "register")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "register")
            is_valid = False
        if len(user['username']) < 2:
            flash("Userame must be at least 2 characters.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be 8 characters or greater.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match", "register")
            is_valid = False
        return is_valid
