# -*- coding:utf-8 -*-
#follow the external links only in parent url and newlinks

from urllib.request import urlopen
from urllib.parse import urlparse   #analyse the url
from bs4 import BeautifulSoup
import re
import datetime
import random
from urllib.error import HTTPError

pages = set()
random.seed(datetime.datetime.now())


# get all the internal links in the page
def getInternalLinks(soup, includeUrl):
    #print('includeUrl 11'+includeUrl)
    #includeUrl = urlparse(includeUrl).scheme + '://' + urlparse(includeUrl).netloc  # DO NOT NEED
    print(includeUrl)
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
    try:
        html = urlopen(startingPage)
        soup = BeautifulSoup(html,'html.parser')
        externalLinks = getExternalLinks(soup, urlparse(startingPage).netloc)
        if len(externalLinks)==0:
            print('No external links, looking around the site for one')
            domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
            internalLinks = getInternalLinks(soup,domain)
            if internalLinks == []:
                print('No more internal and external links! Search finished!')
                return
            else:
                return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
        else:
            elink = externalLinks[random.randint(0,len(externalLinks)-1)]
            print(elink)
            return elink
    except HTTPError as e:
        print(e)
        return


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    if externalLink:
        print("Random external link is: "+externalLink)
        followExternalOnly(externalLink)
    else:
        print('Finished')

followExternalOnly('http://oreilly.com')




