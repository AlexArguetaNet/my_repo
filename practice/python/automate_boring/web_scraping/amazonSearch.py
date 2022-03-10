#! python3
# amazonSearch.py - Open 5 search results from amazon.com

import sys
import requests
import bs4
import webbrowser


# search result selector = .sg-col-inner

res = requests.get('https://www.amazon.com/s?k=cpu')


try:
    res.raise_for_status()
except Exception as e:
    print('STATUS ERROR: ', e)
    sys.exit()





