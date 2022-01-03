
import scrapy

class telegramrEnricher(scrapy.Spider):
    name = "telegramrEnricher"
    start_urls = [l.strip() for l in open('telegrams.txt').readlines()]
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
