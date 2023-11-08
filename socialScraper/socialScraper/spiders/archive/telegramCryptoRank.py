import scrapy

from airscraper import AirScraper

url='https://airtable.com/shrwFxXFcO55sAIGb'

client = AirScraper(url)
data = client.get_table()

with open('telegramFeed.csv','w') as f:
  f.write(data)


import pandas as pd

df = pd.read_csv("telegramFeed.csv")
telegramFeed = df['telegram'].tolist()



class telegramrEnricher(scrapy.Spider):
    name = "telegramrEnricher"
    #start_urls = [l.strip() for l in open('telegrams.txt').readlines()]
    start_urls=telegramFeed

    custom_settings={
    "CONCURRENT_REQUESTS" : "1",
    "DOWNLOAD_DELAY" : "1",
    "CONCURRENT_REQUESTS_PER_DOMAIN" : "1",
    "CONCURRENT_REQUESTS_PER_IP" : "1",
    "AUTOTHROTTLE_ENABLED":"1",
    "AWS_ACCESS_KEY_ID" : 'AKIAT3UE4QVW7SOHMLKM',
    "AWS_SECRET_ACCESS_KEY":'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',

    "FEEDS" : {
        's3://cryptorankbucket/telegramEnriched.csv': {
            'format': 'csv',
            'encoding': 'utf8',
            'store_empty': False,
            'indent': 4,
        }
      },
    "ITEM_PIPELINE" : {
    'scrapy.pipelines.files.S3FilesStore': 1
    },
    "FILES_STORE":'s3://cryptorankbucket/telegramEnriched.csv'
    }




    def parse(self,response):
      data={  }
      data['page'] = response.url
      data['description']= response.css('div.tgme_page_description::text').get()
      try:
            data['telegram_name'] = response.css('div.tgme_page_title>span::text').get()
      except:
            data['telegram_name'] = ''
      try:
            if "members" in response.css('div.tgme_page_extra::text').get():
              data['telegram_members_count'] = response.css('div.tgme_page_extra::text').get().split(', ')[0].split(' members')[0].replace(' ','')
              data['telegram_OnlineMembers_count'] = response.css('div.tgme_page_extra::text').get().split(', ')[1].split(' online')[0].replace(' ','')

            if "subscribers" in response.css('div.tgme_page_extra::text').get():
              data['telegram_members_count'] = response.css('div.tgme_page_extra::text').get().split(', ')[0].split(' subscribers')[0].replace(' ','')
              data['telegram_OnlineMembers_count'] ="0.01"
    
      except:
            data['telegram_members_count'] = ''
            data['telegram_OnlineMembers_count']=''
      yield data   
