from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = re.sub('\n+',' ', input)
    input = re.sub(' +', ' ', input)
    input = re.sub('\[[0-9]*\]','', input)
    input = bytes(input,'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput=[]
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item)>1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input,n):
    output = {}
    for i in range(len(input)-n+1):
        newNgram = ' '.join(input[i:i+n])
        if newNgram in output:
            output[newNgram] +=1
        else:
            output[newNgram] =1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html,'html.parser')
content = soup.find('div',{'id':'mw-content-text'}).get_text()

test = ngrams(cleanInput(content),2)
result = OrderedDict(sorted(test.items(),key=lambda t:t[1], reverse = True))
print(result)
print('2-grams count is: '+str(len(result)))
