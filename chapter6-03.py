from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', {'id':'mw-content-text'}).get_text()
print(content)
content = bytes(content, 'UTF-8')
#print(content)
content = content.decode('UTF-8')
print(content)  # same as the first content