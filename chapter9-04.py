import requests

files = {'uploadFile': r'D:\03-CS\web scraping with python\logo.png'}
r = requests.post('http://pythonscraping.com/pages/processing2.php',files =files)
print(r.text)