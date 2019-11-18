from app import app
import urllib.request,json
from .models import news 
from .models import source
Source = source.Sources

News = news.News


api_key = '92d565a28d7247528cd2a989d0bf3cd5'
base_url = 'https://newsapi.org/v2/sources?apikey={}'
article_url = 'https://newsapi.org/v2/everything?sources={}&apikey={}'

def get_newsSources():
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    
    return news_results



def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        id = news_item.get('id')
        description = news_item.get('description')
        
        source_object = Source(name,id,description)
       
        news_results.append(source_object)
        
    return news_results

def get_articles(source_id):
    get_article_url = article_url.format(source_id,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        
        article_results = None
        
        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_article(article_results_list)
    return article_results

def process_article(article_list):
    article_results=[]
    for article in article_list:
        id = article.get('id')
        urlToImage = article.get('urlToImage')
        url = article.get('url')
        title = article.get('title')
        description = article.get('description')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        
        article_object = News(id,urlToImage,url,title,description,content,publishedAt)
        
        article_results.append(article_object)
    return article_results        
