from flask import render_template
from .requests import get_newsSources,tophigh
from app import app

@app.route('/')
def index():
    tophighlights = tophigh('politics')
    newssources = get_newsSources('sources')
    print(newssources)
    title = 'NewsAway'
    return render_template('index.html',title = title,tophigh = tophighlights,sourcenews = newssources)


@app.route('/news/<int:news_id>')
def news(news_id):
    
    return render_template('news.html',id = news_id)