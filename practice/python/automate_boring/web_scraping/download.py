import requests

# Gets entire script of "Romeo and Juliet" in a .txt file from this URL
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# Checks if the request was succesful or failed
try:
    res.raise_for_status()
except Exception as e:
    print('There was a problem: %s' % (e))

# print(res.text) # print file content

# Cerating file to store requested data. wb = write to binary
playFile = open('practice\\python\\automate_boring\\web_scraping\\rj.txt', 'wb')

# iter_content() returns pieces of byte data. Its arguement is the
# number of bytes it will return.
for i in res.iter_content(1000000):
    playFile.write(i)

playFile.close()

