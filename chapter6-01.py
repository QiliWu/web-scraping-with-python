from urllib.request import urlopen
url = "http://www.pythonscraping.com/pages/warandpeace/chapter1.txt"
textPage = urlopen(url)
print(textPage.read())