import scrapy
import json


class twitterEnricher(scrapy.Spider):
    name = "twitterEnricher"
    #start_urls="https://api.twitter.com/1.1/users/lookup.json?screen_name=Centaurify"
    start_urls = [l.strip() for l in open('twitters.txt').readlines()]
    
    headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAH%2F%2BJQEAAAAA1Jh0N5MBpUO6EnAwgE3Q%2FrQ6xEc%3DHJF5onP5l0Eb400rHCjVGiqm4ODWhSdv5hEEjrxlbOKE2RHZuJ'
    }

    

    def parse(self,response):
      JSON=json.loads(response.body)
      print('################################################')
      print(JSON)
      print('################################################')
      data={}

      
      data['handle']= JSON[0]['screen_name']
      data['twitter_url']="https://twitter.com/"+data['handle']
      data['followers_count']= JSON[0]['followers_count']
      data['friends_count']= JSON[0]['friends_count']
      data['created_at']= JSON[0]['created_at']
      data['profile_image_url']= JSON[0]['profile_image_url']
      data['URLShown']= JSON[0]['entities']['url']['urls'][0]['expanded_url']
  
      data['linksInDescription']= JSON[0]['entities']['description']['urls'][0]['expanded_url']

      data['telegram']=""
      if "t.me" in data['URLShown']:
        data['telegram']=data['URLShown']
      
      if "t.me" in data['linksInDescription']:
        data['telegram']=data['linksInDescription']


      data['description']= JSON[0]['description']

      yield data
      




