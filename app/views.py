from flask import render_template
from app import app


@app.route('/')
def index():
  title = 'Homepage'
  index = 'index.html'
  return render_template(index, title=title)



@app.route('/articles')
def articles():
  title = 'articles'
  articles= 'articles.html'                                                                                                                                                                                              
  return render_template(articles, title=title)


@app.route('/about')
def about():
  title = 'About'
  about= 'about.html'
  return render_template(about, title=title)