
from flask import render_template
from  .import main
from ..requests import get_sources, news_articles



@main.route('/')
def index():
  sources = get_sources()
  
  
  return render_template('index.html',sources=sources)





@main.route('/article/<id>')
def articles(id):

  
  '''
  View articles page
  '''

  articles = news_articles(id)
  
  return render_template('article.html',articles=news_articles)