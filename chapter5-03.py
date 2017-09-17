import csv

csvFile = open('D:/03-CS/web scraping with python/chapter5-03.csv','w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus2','number times2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()