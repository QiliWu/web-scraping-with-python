from urllib.request import urlopen
from io import StringIO
import csv

url = "http://pythonscraping.com/files/MontyPythonAlbums.csv"
data = urlopen(url).read().decode('ascii', 'ignore')
dataFile = StringIO(data)
#csvReader = csv.reader(dataFile)
dictReader = csv.DictReader(dataFile)
#print(dictReader.fieldnames)

for row in dictReader:
    print(type(row))
    print(dict(row))
