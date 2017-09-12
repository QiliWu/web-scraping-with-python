from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

#childrenlist= soup.find('table',{'id':'giftList'}).children   #.children, find all the table's child
#for child in childrenlist:
    #print (child)   # print all <tr> parts

#for sibling in soup.find("table",{'id':'giftList'}).tr.next_siblings:
    #print (sibling)

text = soup.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
print (text)

images = soup.findAll('img',{'src':re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
print (images)  #return a list
for image in images:
    print (image)  # <img src="../img/gifts/img1.jpg"/>
    print (image['src'])   #../img/gifts/img1.jpg-----get image's attr('src')'s content

two_attrs = soup.findAll(lambda tag:len(tag.attrs) == 2)  #output all tags with two attrs
print (two_attrs)