import requests

# Gets entire script of "Romeo and Juliet" in a .txt file from this URL
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.text)
