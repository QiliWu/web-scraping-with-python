#get all the external links in parent url and newlinks

from urllib.request import urlopen
from urllib.parse import urlparse   #analyse the url
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())


# get all the internal links in the page
def getInternalLinks(soup, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc
    internalLinks = []
    # find all links initialized with '/'
    for link in soup.findAll('a', href = re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

# get all the external links in the page
def getExternalLinks(soup, excludeUrl):
    externalLinks = []
    #find all the links initialized with 'http' or 'www' except the current url
    for link in soup.findAll('a', href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    soup = BeautifulSoup(html,'html.parser')
    externalLinks = getExternalLinks(soup, urlparse(startingPage).netloc)
    if len(externalLinks)==0:
        print('No external links, looking around the site for one')
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(soup,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]


# collect all the external links found
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    soup = BeautifulSoup(html, 'html.parser')
    domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
    internalLinks = getInternalLinks(soup,domain)
    externalLinks = getExternalLinks(soup,domain)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            print('now get URL:'+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

allIntLinks.add("http://oreilly.com")
getAllExternalLinks('http://oreilly.com')


print('finished')



