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

print(res.text)
