# beautifulsoup is a module used to
# extract data from webpages. It is imported
# as bs4 (beautifulsoup 4)

import bs4
import requests

res = requests.get('https://nostarch.com')

try:
    res.raise_for_status()
except Exception as e:
    print(e)

# Passing a url as an argument
# BeautifulSoup takes 2 arguments: A string of text, a string of the parsing
#                                  method
noStrachSoup = bs4.BeautifulSoup(res.text, 'html.parser')


exFile = open('practice\\python\\automate_boring\\web_scraping\\html\\example.html')

# Passing the content of an html file 
exSoup = bs4.BeautifulSoup(exFile.read(), 'html.parser')

# Get elements with an id attribute of author
elems = exSoup.select('#author')

print(elems[0].getText()) # Print first element of elems list

# Get all p tag elements
elemsP = exSoup.select('p')
print(elemsP[0].getText())



