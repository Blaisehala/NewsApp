class config :
  '''The configuration parent class'''
  ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  NEWS_URL = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-01&sortBy={}&apiKey={}'



class ProdConfig(config):

  '''The production config child class'''
  pass



class DevConfig(config):
  '''The development config child class'''
  DEBUG = True