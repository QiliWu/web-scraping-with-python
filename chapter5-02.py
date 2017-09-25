import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoulteURL(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://'+source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://'+source[4:]
    else:
        url = baseUrl+'/'+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.','')
    print(path)
    path = path.replace(baseUrl,'')
    print(path)
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    print(path)

    return path

html = urlopen('http://www.pythonscraping.com')
soup = BeautifulSoup(html,'html.parser')
downloadList = soup.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoulteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))

