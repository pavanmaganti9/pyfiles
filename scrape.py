#!c:/Python27/python
print "Content-type: text/html"
print
from bs4 import BeautifulSoup as soup
import request
import urllib3
import urlopen as ureq

url = 'https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone'

uClient = ureq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

Containers = page_soup.findAll("div", {"class":"s-item-container"})

print(len(Containers))