
**CryptoRank Pages ENRICHING COMMANDS**
```
pip install scrapy  
pip install botocore
cd socialScraper/socialScraper/spiders
rm cryptorankEnriched.json
rm cryptorankEnriched.csv
scrapy runspider cryptorankPageExtractor.py -o cryptorankEnriched.json -o cryptorankEnriched.csv
```



**IDO ENRICHING COMMANDS**
```
pip install scrapy  
cd socialScraper/socialScraper/spiders
rm socials.json
rm socials.csv
scrapy runspider idoEnricher.py -o socials.json -o socials.csv
```

**TELEGRAM ENRICHING COMMANDS**
```
pip install scrapy
cd socialScraper/socialScraper/spiders
rm telegram.json
rm telegram.csv
scrapy runspider telegramEnricher.py -o telegram.json -o telegram.csv
```



**TWITTER ENRICHING COMMANDS**
```
pip install scrapy
cd socialScraper/socialScraper/spiders
rm twitter.json
rm twitter.csv
scrapy runspider twitterStrange.py -o twitter.json -o twitter.csv

```



**TW API**
```

API key
X1DytC9zGihUp02milJ8mfcTO
API Secret
uNxX3FEnCYmn3p0gFNFoqKIeMm4kS4mPWOepNDL5V1TigNTZii

Bearer Token
AAAAAAAAAAAAAAAAAAAAAH%2F%2BJQEAAAAA1Jh0N5MBpUO6EnAwgE3Q%2FrQ6xEc%3DHJF5onP5l0Eb400rHCjVGiqm4ODWhSdv5hEEjrxlbOKE2RHZuJ


Access Token
98937372-CO62JQVSkgEhtuiDAGE1ft0dq42KnSleGoqSNdZ3S
Access Secret Token
5hCsXjdVlEFNKAcNDmac6zuYEmoerCMp2hNiZQJdLx7Xc
```



```
User: willaim.jaxxson@ecodaw.com

Zyte Smart Proxy Manager Key: b900e9f653464e23938c8dc9f51c0a89
Zyte Scrapy Cloud Key: 4c210cbc255d48278ba5e367cb67f02d
```

**Commands to deploy**
```
cd socialScraper
pip install shub
shub login
4c210cbc255d48278ba5e367cb67f02d
shub deploy 564603

```
