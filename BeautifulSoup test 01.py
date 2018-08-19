from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
#print (html)   #result:<http.client.HTTPResponse object at 0x00000017AF402438>
#print (type(html))    #result:<class 'http.client.HTTPResponse'>
#print (html.read())
#here, no difference in using html or html.read()， output tree shape html text
soup = BeautifulSoup(html,'html.parser')
#print (soup)   #with tags
#print (soup.text)   #without tags
#print (soup.head)    #bs4.element tag type
#print (type(soup.head))
#print (soup.head.text)
#print (soup.head.get_text())   #text=property(get_text())

namelist = soup.findAll('span',{'class':'green'})  #or ('span', class_='green')
print (namelist)  # output a list, element contain tags

for name in namelist:
    print(name.get_text())   #Anna Pavlovna.  get_text() could remove the tags
    #print (name)   #<span class="green">Anna Pavlovna</span>
    print (name.text)    #same as name.get_text()


headlist = soup.findAll({'h1','h2','h3'})
#print (headlist)   #return [<h1>War and Peace</h1>, <h2>Chapter 1</h2>]

prince_words = soup.findAll(text = 'the prince')   # find all the text "the prince"
#print (prince_words)     #['the prince', 'the prince', 'the prince']

alltext = soup.findAll(id='text')
#print(alltext)  #same as soup, but it is a list with only one element
#print(alltext[0])
#print(alltext[0].get_text())  #delete the tags
