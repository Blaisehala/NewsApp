from app import app 
import urllib.request
import json
from .models import articles,source


Articles = articles.Articles
Sources = source.Source

#  setting up our request
BASE_SOURCE_URL = app.config['NEWS_URL']
api_key = app.config['NEWS_API_KEY']