import scrapy


class twitterEnricher(scrapy.Spider):
    name = "twitterEnricher"
    #start_urls="https://api.twitter.com/1.1/users/lookup.json?screen_name=Centaurify"

    start_urls = [l.strip() for l in open('strangeTwitter.txt').readlines()]
    
    custom_settings={
    "CONCURRENT_REQUESTS" : "1",
    "DOWNLOAD_DELAY" : "1",
    "CONCURRENT_REQUESTS_PER_DOMAIN" : "1",
    "CONCURRENT_REQUESTS_PER_IP" : "1",
    "AUTOTHROTTLE_ENABLED":"1",
    "AWS_ACCESS_KEY_ID" : 'AKIAT3UE4QVW7SOHMLKM',
    "AWS_SECRET_ACCESS_KEY":'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',

    "FEEDS" : {
        's3://cryptorankbucket/twitterEnriched.csv': {
            'format': 'csv',
            'encoding': 'utf8',
            'store_empty': False,
            'indent': 4,
        }
      },
    "ITEM_PIPELINE" : {
    'scrapy.pipelines.files.S3FilesStore': 1
    },
    "FILES_STORE":'s3://cryptorankbucket/twitterEnriched.csv'
    }
    

    def parse(self,response):
      print('################################################')
      
      data={}

      data['twitter_url']=response.url
      data['followerCount']=response.css('li.followers>span.profile-stat-num::text').get().replace(',',"")

      print('################################################')

      yield data
      




