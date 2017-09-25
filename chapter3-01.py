#collect the all the links in a url,the results contain a lot of unusable information

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html,'html.parser')

for link in soup.findAll('a'):
    print (link.attrs)   #print all the attrs of link
    if 'href' in link.attrs:
        print(link.attrs['href'])


#

