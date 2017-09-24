import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup

class TestWikipedia(unittest.TestCase):
    html = urlopen("http://en.wikipedia.org/wiki/Monty_Python")
    soup = BeautifulSoup(html, 'html.parser')

    def test_titleTest(self):
        title = self.soup.find('h1').get_text()
        self.assertEqual('Monty Python', title)

    def test_contentTest(self):
        content = self.soup.find('div', {'id':'mw-content-text'})
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()