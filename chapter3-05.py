#collect all the links in parent url and newlinks  with exception consideration

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    soup = BeautifulSoup(html,'html.parser')

    try:
        print(soup.h1.get_text())
        print(soup.find(id='mw-content-text').findAll('p')[0])
        print(soup.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("Page lacks some attrs, but don't worry!")

    for link in soup.findAll('a', href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # it's a new page
                newPage = link.attrs['href']
                print('-'*20+'\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')

print('finished')



