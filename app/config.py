class Config:
    
  NEWS_API = 'https://newsapi.org/v2/{}?apikey={}'

class ProdConfig(Config):
    
    pass

class DevConfig(Config):
    
    DEBUG = True