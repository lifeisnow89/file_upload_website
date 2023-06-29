from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

class File:
    db = 'users'
    def __init__(self, data):
        self.id = data['files_id']
        self.file_name = data['file_name']
        self.size = data['size']
        self.extension = data['extension']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.posted_by = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO files (file_name, size, extension, users_user_id) VALUES (%(file_name)s, %(size)s, %(extension)s, %(user_id)s)"
        result = connectToMySQL('graduation_project').query_db(query, data)
        return result
        
    @classmethod
    def get_all(cls, user_id):
        query = "SELECT * FROM files WHERE users_user_id=%(user_id)s"
        data = {
            "user_id": user_id
        }
        results = connectToMySQL('graduation_project').query_db(query, data)
        files = []
        for file in results:
            files.append(cls(file))

        return files
    
    @classmethod
    def get_everything(cls):
        query = "SELECT * FROM files LEFT JOIN users ON files.users_user_id = users.user_id;"
        results = connectToMySQL('graduation_project').query_db(query)
        print(results)
        files = []
        for file in results:
            new_file = cls(file)
            new_file.posted_by = file['username']
            files.append(new_file)
        return files
    
    @classmethod
    def get_file_w_user(cls, user_id):
        data = {'user_id' : user_id}
        query = "SELECT * FROM files LEFT JOIN users ON files.users_user_id = users.user_id WHERE files.id = %(files_id)s;"
        results = connectToMySQL('graduation_project').query_db(query, data)
        files = cls(results[0])
        print(results[0])
        files.posted_by = results[0]['username'] 
        print('*************************', 
            files.posted_by, 
        '***********************************')
        return files 
