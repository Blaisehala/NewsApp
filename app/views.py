from flask import render_template
from app import app
from app.requests import news_articles



@app.route('/')
def index():
  sports_news= news_articles('sports')
  health_news= news_articles('health')
  entertainment_news= news_articles('entertainment')
  business_news= news_articles('business')
  
  return render_template('index.html',sports=sports_news, health=health_news, entertainment=entertainment_news,business=business_news)


