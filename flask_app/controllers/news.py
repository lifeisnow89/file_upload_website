from flask import redirect, render_template, request, send_from_directory, abort, jsonify, url_for, session
from flask_app import app
import requests
import os
from flask import jsonify

@app.route('/news')
def get_news():
    r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={os.environ.get ('FLASK_API_KEY')})/get_news?={request.form['query']}")
    return jsonify( r.json())

print( os.environ.get("FLASK_APP_API_KEY") )