import scrapy
from airscraper import AirScraper
import boto3


url='https://airtable.com/shrwFxXFcO55sAIGb'

client = AirScraper(url)
data = client.get_table()

with open('twitterFeed.csv','w') as f:
  f.write(data)


import pandas as pd



df = pd.read_csv("twitterFeed.csv",sep=',')

# converting column data to list
twitterFeed = df['twitterstrange'].tolist()


print(twitterFeed)

class twitterEnricher(scrapy.Spider):
    name = "twitterEnricher"
    start_urls = twitterFeed
    
    custom_settings={
    "CONCURRENT_REQUESTS" : "1",
    "DOWNLOAD_DELAY" : "0.2",
    "CONCURRENT_REQUESTS_PER_DOMAIN" : "1",
    "CONCURRENT_REQUESTS_PER_IP" : "1",
    "AUTOTHROTTLE_ENABLED":"0",
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
      




#Exporting
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAT3UE4QVW7SOHMLKM',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

object = s3.Object('cryptorankbucket', 'twitterEnriched.csv')

result = object.put(Body=open('twitterEnriched.csv', 'rb'))

res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')