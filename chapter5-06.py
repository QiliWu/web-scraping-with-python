from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       passwd='wuqili2017',db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")",(title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1').get_text()
    print(title)
    content = soup.find('div', {'id':'mw-content-text'}).find('p').get_text()
    print(content)
    store(title, content)
    return soup.find('div', {'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')

try:
    while len(links)>0:
        newArticle = links[random.randint(0,len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    conn.close()