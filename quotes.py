import requests as rq
from bs4 import BeautifulSoup

qheader = {
    
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
qurl='https://books.toscrape.com/'

qresp=rq.get(url=qurl,headers=qheader)

qsoup=BeautifulSoup(qresp.content,'html.parser')

qtitle=qsoup.a

print("qtitle",qtitle)

anchors_tG=qsoup.findAll('a',title=True)

for anchor in anchors_tG:
    book_title=anchor['title']
   
    print('Title:',book_title)
    
    
    
priceList = qsoup.findAll('p', attrs={'class': 'price_color'})
#print('priceList',priceList)
print()
print()
bookPrice = [price.text for price in priceList]

print('book price', bookPrice)

print()
ratingList = qsoup.findAll('p', attrs={'class': 'star-rating'})

for rating in ratingList:
 print('rating',rating['class'][1])
