import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
           'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           'Accept-Encoding': "gzip, deflate, br"}

url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"

session = requests.Session()

r = session.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
print(soup.find('table', {'class': 'table-striped'}).get_text)