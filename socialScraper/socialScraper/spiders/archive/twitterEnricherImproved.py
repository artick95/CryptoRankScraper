import scrapy
import json


class twitterNEW(scrapy.Spider):
    name = "twitterNEW"

    my_list = list([l.strip() for l in open('twitters.txt').readlines()])
    
    splitted_list=[]
    n=100
    #for i in range(0, len(my_list), n): 
   #   splitted_list[i]=my_list[i:i + n]
    # print(splitted_list)
    #  print(i)

    #print(splitted_list)
    #print("####################################")

    #urls="https://api.twitter.com/2/users/by?usernames="+','.join(handles[0])
    #print(urls)
    




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
      




