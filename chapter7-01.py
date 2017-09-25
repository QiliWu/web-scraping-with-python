from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(input, n):
    input = re.sub('\n+', ' ', input)  # 去掉连续转义字符\n
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


# 消除转义字符的是下一行代码的ignore参数，转义字符因为不能被ascii decode，如果不加ignore就会报错，加了ignore就会被忽略。
# contents是一个str，由一系列不可改变的Unicode字符组成，本身不能被decode，用utf8 encode之后转为bytes才可以被decode。
# encode是转为计算机能理解的二进制数，bytes就是一系列不可改变的介于0-255之间的数字。decode就是转为我们可以理解的字符。
# ascii字符集远小于unicode字符集，用ascii decode的时候那些不在ascii字符集的字符就会导致报错，设了ignore参数后就会被忽略。
