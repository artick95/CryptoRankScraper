import scrapy
from pandas import *
 
# reading CSV file
data = read_csv("https://rss.app/feeds/YsCY0cZumXPuPMhN.csv")

# converting column data to list
newUrls = data['Link'].tolist()
start_urls = [l.strip() for l in open('cryptoRankPages.txt').readlines()]
start_urls=newUrls+ start_urls


class cryptorank(scrapy.Spider):
    
    name = "cryptorank"
    user_agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    #start_urls = [l.strip() for l in open('cryptoRankPages.txt').readlines()]
    start_urls = start_urls
 



    def parse(self,response):
      data={  }
      data['page'] = response.url
      try:
            data['website'] = response.css('div.coin-info__CoinIconLinksBlock-sc-ag81st-0>a::attr(href)').get()
      except:
            data['website'] = ''    

            
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
            data['whitepaper'] =  response.xpath('//a[contains(@href, "whitepaper.pdf")]/@href').extract()
            data['litepaper'] =  response.xpath('//a[contains(@href, "litepaper.pdf")]/@href').extract()
            data['tokenomics'] =  response.xpath('//a[contains(@href, "tokenomics.pdf")]/@href').extract()
            data['deck'] =  response.xpath('//a[contains(@href, "deck.pdf")]/@href').extract()
            data['pitch'] =  response.xpath('//a[contains(@href, "pitch.pdf")]/@href').extract()
            data['pitchdeck'] =  response.xpath('//a[contains(@href, "pitchdeck.pdf")]/@href').extract()
            data['presentation'] =  response.xpath('//a[contains(@href, "presentation.pdf")]/@href').extract()            

      except:
            data['whitepaper'] = ''
            data['whitepaper'] =  ''
            data['litepaper'] =  ''
            data['tokenomics'] =  ''
            data['deck'] =  ''
            data['pitch'] =   ''
            data['pitchdeck'] =   ''
            data['presentation'] =  ''           

      try:
            data['linkedin_urls'] =  response.xpath('//a[contains(@href, "linkedin.com/")]/@href').extract()            
      except:
            data['linkedin_urls'] = ''
      try:
            data['email']= response.xpath('//a[contains(@href, "mailto")]/@href').get().split(':')[1]      
      except:
             data['email']=""
    

      yield data   
