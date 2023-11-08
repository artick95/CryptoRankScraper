from airscraper import AirScraper

url='https://airtable.com/shrwFxXFcO55sAIGb'

client = AirScraper(url)
data = client.get_table()

# save as file
with open('twitterFeed.csv','w') as f:
  f.write(data)

with open('twitterFeed.csv','w') as f:
  f.write(data)




