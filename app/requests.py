import urllib.request
import json
from  .models import articles


# Articles = articles.Articles
# Sources = source.Source

#  setting up our request
# BASE_SOURCE_URL = app.config['NEWS_URL']
# BASE_ARTICLES_URL = app.config['ARTICLES_URL']
# api_key = app.config['NEWS_API_KEY']

def configure_request(app):
    global api_key,BASE_SOURCE_URL,BASE_ARTICLES_URL
    BASE_SOURCE_URL = app.config['SOURCE_URL']
    BASE_ARTICLES_URL = app.config['ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']



def news_articles(id):
  news_url =  BASE_ARTICLES_URL.format(id,api_key)
#opening the data, reading it and passing it as a dict
  with urllib.request.urlopen(news_url) as projectnews:
    # Reading the project news
    projectnews_data = projectnews.read()

    projectnews_data_dict = json.loads(projectnews_data)
    #  Json.loads converts into a dictionary 


    articles_results = None


    if projectnews_data_dict['articles']:
        articles_list = projectnews_data_dict['articles']
        articles_results = process_results(articles_list)
                
    return articles_results


def process_results(results):
    articles_results = []
    for result in results:
        image = result['urlToImage']
        description = result['description']
        time = result['publishedAt']

        if image:
            articles_object = Articles(image, description, time)
            articles_results.append(articles_object)

    return articles_results
