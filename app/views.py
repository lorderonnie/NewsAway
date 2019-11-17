from flask import render_template
from app import app

@app.route('/')
def index():
       
    title = 'Home - Welcome to the most accessable news site in the world'
    return render_template('index.html',title = title)


@app.route('/news/<int:news_id>')
def news(news_id):
    
    return render_template('news.html',id = news_id)