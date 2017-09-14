#find the IPaddresses with the corresponding countries in the history edit page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random
import json

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('div',{'id':'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    # URL of the history edit page is:
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+'&action=history'
    print("history url is: "+historyUrl)
    html = urlopen(historyUrl)
    soup = BeautifulSoup(html,'html.parser')
    #find the links with class attrs as "mw-userlink mw-anonuserlink'
    #use IPaddress to replace the usename
    ipAddresses = soup.findAll('a',{'class':'mw-userlink mw-anonuserlink'})
    addresslist = set()
    for ipAddress in ipAddresses:
        addresslist.add(ipAddress.get_text())
    return addresslist

def getCountry(ipAddress):
    try:
        response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')

links = getLinks('/wiki/Python_(programming_language)')

while len(links)>0:
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+' is from '+country)

    newLink = links[random.randint(0,len(links)-1)].attrs['href']
    links = getLinks(newLink)