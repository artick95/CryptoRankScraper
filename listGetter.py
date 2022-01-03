from pandas import *
 
# reading CSV file
data = read_csv("https://rss.app/feeds/YsCY0cZumXPuPMhN.csv")
start_urls = [l.strip() for l in open('cryptoRankPages.txt').readlines()]
 
# converting column data to list
newUrls = data['Link'].tolist()

start_urls=newUrls+ start_urls

print("new urls####################\n")
print( newUrls)

print("start urls####################\n")
print(start_urls)
