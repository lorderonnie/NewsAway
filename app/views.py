from flask import render_template
from app import app

@main.route('/')
def index():
    
    
    return render_template('index.html')