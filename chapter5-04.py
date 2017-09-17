import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
soup = BeautifulSoup(html, 'html.parser')

table = soup.findAll('table',{'class':'wikitable'})[0]
print(table)
rows = table.findAll('tr')

csvFile = open('D:/03-CS/web scraping with python/chapter5-04.csv','wt',
               newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()