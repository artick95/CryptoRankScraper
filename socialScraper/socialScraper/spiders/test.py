import scrapy
from pandas import *
 
# reading CSV file
data = read_csv("https://cryptorank.s3.us-east-2.amazonaws.com/newsfeedcryptorank.csv")

# converting column data to list
newUrls = data['links'].tolist()
start_urls = [l.strip() for l in open('test.txt').readlines()]
start_urls=newUrls + start_urls
start_urls=list(dict.fromkeys(start_urls))

f = open("test.txt",'w')

for element in start_urls:
    f.write(element + "\n")
f.close()



from urllib.parse import urlparse

domain = urlparse('https://ertha.io?utm_source=cryptorank').netloc

if "www." in domain:
  domain = domain.split('www.')[1]



print(domain) # --> www.example.test