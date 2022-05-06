import urllib.request
import json
from .models import Articles,Source


BASE_ARTICLES_URL= None
SOURCE_URL= None
api_key = None

def configure_request(app):
  global api_key,BASE_ARTICLES_URL,SOURCE_URL
  
  api_key = app.config['NEWS_API_KEY']
  SOURCE_URL= app.config['SOURCE_URL']
  BASE_ARTICLES_URL= app.config['BASE_ARTICLES_URL']

def get_sources():
  get_source_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=a47ff0739316461ca947d81c376a58c3'
#opening the data, reading it and passing it as a dict
  with urllib.request.urlopen(get_source_url) as news_source:
    # Reading the source data
    source_data = news_source.read()
    source_data_dict = json.loads(source_data)
    # Json.loads converts into a dictionary 
    # print(source_data_dict)

    source_results = None  

    if source_data_dict['sources']:
      sources_list = source_data_dict['sources']
      source_results = process_sources(sources_list)

  return source_results

def process_sources (sources):
  sources_list = []
  for source in sources:
  
    id = source['id']
    name = source['name']
    description = source['description']
    url = source['url']

    if url:
      source_object = Source(id,name, description,url)
      sources_list.append(source_object)

  return sources_list





# class Articles 

def get_articles(id):
  get_articles_url = BASE_ARTICLES_URL.format(id)
  with urllib.request.urlopen(get_articles_url) as articles_content:
    articles_data = articles_content.read()
    articles_dict =json.loads(articles_data)
    

    articles_results = None

    if articles_dict['articles']:
      articles_list = articles_dict['articles']
      articles_results = process_articles(articles_list)

  return articles_results

def process_articles(list):
  articles_results = [] 

  for article in list:
    urlToImage = article['urlToImage']
    description = article['description']
    publishedAt = article['publishedAt']
    title = article['title']
    url = article['url']

    if urlToImage:
      articles_object = Articles(urlToImage,description,publishedAt,title,url)
      articles_results.append(articles_object)

  return articles_results

    



