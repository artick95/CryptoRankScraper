
import scrapy

class telegramEnricher(scrapy.Spider):
    name = "telegramEnricher"
    start_urls = ['https://t.me/emergencycrypto']



    def parse(self,response):
      data={  }
      data['page'] = response.url
      try:
            data['discord_urls'] = response.xpath('//a[contains(@href, "discord.gg")]/@href').extract()
      except:
            data['discord_urls'] = ''
      try:
            data['twitter_urls'] = response.xpath('//a[contains(@href, "twitter.com")]/@href').extract()
      except:
            data['twitter_urls'] = ''
      try:
            data['telegram_urls'] = response.xpath('//a[contains(@href, "t.me")]/@href').extract()
      except:
            data['telegram_urls'] = ''
      try:
            data['ticktok_urls'] = response.xpath('//a[contains(@href, "tiktok.com")]/@href').extract()
      except:
            data['ticktok_urls'] = ''
      try:
            data['instagram_urls'] = response.xpath('//a[contains(@href, "instagram.com")]/@href').extract()
      except:
            data['instagram_urls'] = ''
      try:
            data['youtube_urls'] = response.xpath('//a[contains(@href, "youtube.com")]/@href').extract()
      except:
            data['youtube_urls'] = ''
      try:
            data['whitepaper'] = response.xpath('//a[contains(@href, "whitepaper.pdf")]/@href').extract()
      except:
            data['whitepaper'] = ''
    
    

      yield data   
