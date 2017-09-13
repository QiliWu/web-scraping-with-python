#collect a random link at each depth

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


random.seed(datetime.datetime.now())

def getLinks(articleUrl):

    html = urlopen("http://en.wikipedia.org"+articleUrl)
    soup = BeautifulSoup(html,'html.parser')

    return soup.find('div',{'id':'bodyContent'}).findAll\
                         ('a', href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

print('finished')



