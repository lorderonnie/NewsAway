from flask import render_template
from .requests import get_newsSources,get_articles
from app import app

@app.route('/')
def index():
    newssources = get_newsSources()
    print(newssources)
    title = 'NewsAway'
    return render_template('index.html',title = title,sourcenews = newssources)


@app.route('/news/<news_id>')
def article(news_id):
    articles = get_articles(news_id)
    return render_template('news.html',articles = articles,id = news_id)