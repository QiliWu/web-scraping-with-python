from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(input, n):
    input = re.sub('\n+', ' ', input)  # 去掉连续转义字符
    input = re.sub(' +', ' ', input)   # 去掉连续空格
    input = bytes(input,'UTF-8')
    input = input.decode('ascii', 'ignore')
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(html,'html.parser')
content = soup.find('div',{'id':'mw-content-text'}).get_text()
test = ngrams(content,2)
print(test)
print('2-grams count is: '+str(len(test)))
