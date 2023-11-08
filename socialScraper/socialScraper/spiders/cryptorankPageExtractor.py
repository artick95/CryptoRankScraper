import scrapy
from pandas import *

from urllib.parse import urlparse


 
# reading CSV file
#data = read_csv("https://rss.app/feeds/YsCY0cZumXPuPMhN.csv")
data = read_csv("https://cryptorank.s3.us-east-2.amazonaws.com/newsfeedcryptorank.csv")

# converting column data to list
newUrls = data['links'].tolist()
start_urls = [l.strip() for l in open('cryptoRankPages.txt').readlines()]
start_urls=newUrls + start_urls

#removing duplicates
start_urls=list(dict.fromkeys(start_urls))

f = open("cryptoRankPages.txt",'w')

for element in start_urls:
    f.write(element + "\n")
f.close()



class cryptorank(scrapy.Spider):
    
    name = "cryptorank"
    user_agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    #start_urls = [l.strip() for l in open('cryptoRankPages.txt').readlines()]
    start_urls = start_urls
 
 
    def parse(self,response):
      data={  }
      data['domain']=''
      
      data['page'] = response.url
      try:
            data['website']=response.css('div.coin-info__CoinIconLinksBlock-sc-ag81st-0>a::attr(href)').get()
      except:
            data['website'] = '' 


      try:
        data['domain'] = urlparse(data['website']).netloc

        #correction to remove www
        if "www." in data['domain']:
          data['domain'] = urlparse(data['website']).netloc.split('www.')[1]

      except:
            data['domain']=''   

      try:
            data['IXOprice'] = response.css('div.columns__Column-sc-1g8p74z-1>div::text').get().split('$ ')[1]
      except:
            data['IXOprice'] = '' 

      try:
            data['currentPrice'] = response.css('div.styled__CoinPrice-sc-9jm877-5::text').get().split('USD ')[1]
      except:
            data['currentPrice'] = '' 

      try:
        data['ROI']=response.css('div.columns__Column-sc-1g8p74z-1>div::text').extract()[3].split("x")[0]
      except:
        data['ROI']=""


      try:
            data['discord_urls'] = response.xpath('//a[contains(@href, "discord.gg/")]/@href').get()
      except:
            data['discord_urls'] = ''
      try:
            data['twitter_urls'] = response.xpath('//a[contains(@href, "twitter.com/")]/@href').get()
      except:
            data['twitter_urls'] = ''
      try:
            data['telegram_urls'] = response.xpath('//a[contains(@href, "t.me/")]/@href').get()
            if "join" in data['telegram_urls']:
                data['telegram_urls']=""
            if "announcement" in data['telegram_urls']:
                data['telegram_urls']=""
      except:
            data['telegram_urls'] = ''
      try:
            data['ticktok_urls'] = response.xpath('//a[contains(@href, "tiktok.com/")]/@href').get()
      except:
            data['ticktok_urls'] = ''
      try:
            data['instagram_urls'] = response.xpath('//a[contains(@href, "instagram.com/")]/@href').get()
      except:
            data['instagram_urls'] = ''
      try:
            data['facebook_urls'] = response.xpath('//a[contains(@href, "facebook.com/")]/@href').get()
      except:
            data['facebook_urls'] = ''
      try:
            data['youtube_urls'] = response.xpath('//a[contains(@href, "youtube.com/")]/@href').get()
      except:
            data['youtube_urls'] = ''
      try:
            data['github_urls'] = response.xpath('//a[contains(@href, "github.com/")]/@href').get()
      except:
            data['github_urls'] = ''       

      try:
            data['linkedin_urls'] =  response.xpath('//a[contains(@href, "linkedin.com/")]/@href').extract()            
      except:
            data['linkedin_urls'] = ''
            
      yield data   



