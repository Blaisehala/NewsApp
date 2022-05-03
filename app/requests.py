import urllib.request
import json
from .models import Articles,Source


BASE_ARTICLES_URL= None
SOURCE_URL= None
api_key = None

def configure_request(app):
  global api_key,BASE_ARTICLES_URL,SOURCE_URL
  BASE_ARTICLES_URL = app.config['ARTICLES_URL']
  api_key = app.config['NEWS_API_KEY']
  SOURCE_URL= app.config['SOURCE_URL']


def get_sources():
  source_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=5cec8bf6c5664591a5d11a20c15e1ae4'
#opening the data, reading it and passing it as a dict
  with urllib.request.urlopen(source_url) as news_source:
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

def news_articles(id):
  news_url = BASE_ARTICLES_URL.format(id,api_key)
#opening the data, reading it and passing it as a dict
  with urllib.request.urlopen(news_url) as url:
# Reading the project news
   projectnews_data = url.read()

   projectnews_data_dict = json.loads(projectnews_data)
# Json.loads converts into a dictionary 

   articles_results = None
   if projectnews_data_dict['articles']:
      articles_list = projectnews_data_dict['articles']
      articles_results = process_results(articles_list)
  return articles_results


def process_results(results_list):
  articles_results = []
  for result in results_list:
    urlToImage = result.get('urlToImage')
    description = result.get('description')
    publishedAt = result.get('publishedAt')
    title = result.get('title')
    url = result.get('url')

    if urlToImage:
      articles_object = Articles(urlToImage, description, publishedAt,title,url)
      articles_results.append(articles_object)

  return articles_results









