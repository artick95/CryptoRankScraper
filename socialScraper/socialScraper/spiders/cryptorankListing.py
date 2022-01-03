

import scrapy

class cryptorankListing(scrapy.Spider):
    
    name = "cryptorankListing"
    user_agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    #start_urls = [l.strip() for l in open('cryptoRankPages.txt').readlines()]
    start_urls = ["https://cryptorank.io/ico"]


    def parse(self,response):
      data={  }
      data['page'] = response.url
      data['projectLink']=""

      try:
            data['projectLink'] ="https://cryptorank.io/ico"+ response.css('tr.styled__WrappedTableRow-sc-oiryw1-1>td.nametd>div>a::attr(href)').get()
      except:
            data['website'] = ''    

    

      yield data   
