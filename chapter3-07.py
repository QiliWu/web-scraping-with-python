#get all the external links in parent url and new internallinks

from urllib.request import urlopen
from urllib.parse import urlparse   #analyse the url
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError


# get all the internal links in the page
def getInternalLinks(soup, includeUrl):
    #includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc  # DO NOT NEED
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

# collect all the external links found
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    while len(allExtLinks) < 100:
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
                try:
                    getAllExternalLinks(link)
                except HTTPError as e:
                    print(e)
                    continue

allIntLinks.add("http://oreilly.com")
getAllExternalLinks('http://oreilly.com')


print('finished')



