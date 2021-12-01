

import scrapy

class socialScraper(scrapy.Spider):
    
    name = "socialScraper"
    user_agent="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    start_urls = [l.strip() for l in open('urls.txt').readlines()]


    def parse(self,response):
      data={  }
      data['page'] = response.url
      data['responseStatus']=response.status
      data['metaDescription']= response.xpath("//meta[@name='description']/@content").get()
      data['loadingTime']=response.meta['download_latency']
      data['H1']= response.xpath('//h1//text()').extract_first()
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
