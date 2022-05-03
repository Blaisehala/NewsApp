class Articles:
  def __init__(self,urlToImage, description, publishedAt,title,url):
  
  
    self.urlToImage = urlToImage
    self.description = description
    self.publishedAt = publishedAt
    self.title = title
    self.url = url

class Source:
  def __init__(self,id,name, description,url):
    self.id= id
    self.name= name
    self.description= description 
    self.url = url