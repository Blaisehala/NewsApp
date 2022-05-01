from flask import render_template
from app import app
from .requests import news_articles


@app.route('/')
def index():
  title = 'Homepage'
  index = 'index.html'
  return render_template(index, title=title)



@app.route('/articles/')
def articles(id):
  title = 'articles'
  articles= 'articles.html'
  n_articles = news_articles(id)                                                                                                                                                                                          
  return render_template(articles, title=title, articles = n_articles)


@app.route('/about')
def about():
  title = 'About'
  about= 'about.html'
  return render_template(about, title=title)