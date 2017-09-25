# collect the entry links in a url

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(html,'html.parser')

#for link in soup.find('div',{'id':'bodyContent'}).findAll\
            #('a', href = re.compile("^(/wiki/)((?!:).)*$")):

# or

for link in soup.find('div',{'id':'bodyContent'}).findAll\
            ('a', {'href': re.compile("^(/wiki/)((?!:).)*$")}):
    print(link.attrs['href'])
    if 'href' in link.attrs:   #do not need this step since all the <a> have href
        print(link.attrs['href'])


#the results contain a lot of unusable information

