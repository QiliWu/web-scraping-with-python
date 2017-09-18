from urllib.request import urlopen

url = "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt"
textPage = urlopen(url)
#print(textPage.read())
print(str(textPage.read(),'utf-8'))  #change the sting to utf-8 type