from bs4 import BeautifulSoup
from urllib.request import urlopen
import unittest
import random
import re

class TestWikipedia(unittest.TestCase):
    soup = None
    url = None

    def test_Pageproperties(self):
        global soup
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        for i in range(10):
            soup = BeautifulSoup(urlopen(url),'html.parser')
            titles = self.titleMatchesURL()
            self.assertEqual(titles[0],titles[1])
            self.assertTrue(self.contentExists())
            url = self.getNextLinks()
        print('Done')

    def titleMatchesURL(self):
        global soup
        global url

        pageTitle = soup.find('h1').get_text()
        urlTitle = url[(url.index('/wiki/')+6):]
        urlTitle = urlTitle.replace('_',' ')
       # urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global soup
        global url

        content = soup.find('div', {'id':'mw-content-text'})
        if content is not None:
            return True
        return False

    def getNextLinks(self):

        links = soup.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))
        print(len(links))
        if len(links)>0:
            newlink = 'http://en.wikipedia.org'+links[random.randint(0,len(links)-1)].attrs['href']
            print(newlink)
            return newlink


if __name__ == '__main__':
    unittest.main()






