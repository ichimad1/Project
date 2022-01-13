import scrapy
class MySpider(scrapy.Spider):
  name = "MySpider"
  # start_requests method
  def start_requests(self):
    urls = ["https://www.pitchfork.com"]
    for url in urls:
      yield url
  # parse function
  def parse( self, response ):
    pass
