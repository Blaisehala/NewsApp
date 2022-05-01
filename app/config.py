class config :
  '''The configuration parent class'''

  NEWS_URL = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-01&sortBy={}&apiKey={}'


class DevConfig:
  '''The development config child class'''
  pass

class ProdConfig:

  '''The production config child class'''
  pass

