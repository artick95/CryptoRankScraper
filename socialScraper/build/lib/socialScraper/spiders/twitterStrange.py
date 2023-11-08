import scrapy




class twitterEnricher(scrapy.Spider):
    name = "twitterEnricher"
    #start_urls="https://api.twitter.com/1.1/users/lookup.json?screen_name=Centaurify"

    start_urls = [l.strip() for l in open('strangeTwitter.txt').readlines()]
    
    headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAH%2F%2BJQEAAAAA1Jh0N5MBpUO6EnAwgE3Q%2FrQ6xEc%3DHJF5onP5l0Eb400rHCjVGiqm4ODWhSdv5hEEjrxlbOKE2RHZuJ'
    }

    

    def parse(self,response):
      print('################################################')
      
      data={}

      data['twitter_url']=response.url
      data['followerCount']=response.css('li.followers>span.profile-stat-num::text').get().replace(',',"")

      print('################################################')

      yield data
      




