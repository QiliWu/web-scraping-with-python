from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
soup = BeautifulSoup(html,'html.parser')
imageLocation = soup.find('a',id='logo').find('img')['src']
urlretrieve(imageLocation,'logo.jpg')
#download the logo.jpg, and put it in the current directory