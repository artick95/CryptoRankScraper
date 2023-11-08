import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

import boto3


class listingSpider(Spider):
    name = 'lister'
    start_urls = ['https://cryptorank.io/ico']
    base_url = 'https://cryptorank.io'

    custom_settings={
    "AWS_ACCESS_KEY_ID" : 'AKIAT3UE4QVW7SOHMLKM',
    "AWS_SECRET_ACCESS_KEY":'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',

    "FEEDS" : {
        's3://cryptorankbucket/newsfeedcryptorank.csv': {
            'format': 'csv',
            'encoding': 'utf8',
            'store_empty': False,
            'indent': 4,
        }
    },
    "ITEM_PIPELINE" : {
    'scrapy.pipelines.files.S3FilesStore': 1
    },
    "FILES_STORE":'s3://cryptorankbucket/newsfeedcryptorank.csvv'
  }

    def parse(self, response):
      data={}
      data['links']=[]
      for link in response.xpath('//a[contains(@href, "/ico/")]/@href').extract():
        data['links']=self.base_url+link
        yield response.follow(url=link, callback=self.parse)
      yield data




#Exporting
#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIAT3UE4QVW7SOHMLKM',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

object = s3.Object('cryptorankbucket', 'newsfeedcryptorank.csv')

result = object.put(Body=open('newsfeedcryptorank.csv', 'rb'))

res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')
else:
    print('File Not Uploaded')


