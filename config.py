import os

class Config:
  '''The configuration parent class'''
  ARTICLES_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey=a47ff0739316461ca947d81c376a58c3' 
  SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):

  '''The production config child class'''
  pass



class DevConfig(Config):
  '''The development config child class'''
  DEBUG = True


config_options ={
  "development":DevConfig,
  "production":ProdConfig
}