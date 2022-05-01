from flask import render_template
from app import app


@app.route('/')
def index():
  index = 'index.html'
  return render_template(index)



@app.route('/articles')
def articles():
  return render_template('articles.html')