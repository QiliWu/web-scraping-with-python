from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleanInput(input):
    input = re.sub('\n+',' ', input)    # replace multi \n with single space
    input = re.sub(' +', ' ', input)    #replace multispace with single space
    input = re.sub('\[[0-9]*\]','', input)   # delete [1] type characters
    input = bytes(input,'UTF-8')      # encode unicode string to bytes
    input = input.decode('ascii', 'ignore')     #decode bytes to ascii and ignore the unascii character
    cleanInput=[]
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)   # delete the punctuations at the beginning and ending of item
        if len(item)>1 or (item.lower() == 'a' or item.lower() == 'i'):   # exclude single character except 'a' and 'i'
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html,'html.parser')
content = soup.find('div',{'id':'mw-content-text'}).get_text()

test = ngrams(cleanInput(content),2)
print(test)
print('2-grams count is: '+str(len(test)))
