#! python3
# searchpy.py - Opens several search results

import requests
import sys
import webbrowser
import bs4

print('Searching...')

res = requests.get('https://pypi.org/search/?q=' \
                    + ' '.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as e:
    print('STATUS ERROR: ', e)


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)