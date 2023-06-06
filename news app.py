import requests
import json
t = input('What type of news do you want:')
url = f'https://newsapi.org/v2/everything?q={t}&from=2023-03-13&sortBy=publishedAt&apiKey=014d6c87d703491983e3b6da76401ff8'
r = requests.get(url)
data = json.loads(r.text)
print (data)