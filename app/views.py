from flask import render_template
from .requests import get_news
from app import app

@app.route('/')
def index():
    latest_news = get_news('latest')
    political_news = get_news('political')
    sport_news =   get_news('sport')
    social_news =  get_news('social')   
    title = 'NewsAway'
    return render_template('index.html',title = title,latest = latest_news,political = political_news,sport = sport_news,social = social_news)


@app.route('/news/<int:news_id>')
def news(news_id):
    
    return render_template('news.html',id = news_id)