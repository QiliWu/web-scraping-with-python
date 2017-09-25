from nltk import FreqDist
from nltk.book import *
from nltk import bigrams
from nltk import ngrams

fdist = FreqDist(text6)   # 计算每个单词出现的次数，给出字典，{key:val}={char:count}
print(fdist.most_common(10))    # 10个出现最多次的次
print(type(fdist))    #<class 'nltk.probability.FreqDist'>
print(fdist['Grail'])    # 给出'Grail'出现的次数

bigrams = bigrams(text6)   # 二元分词
bigramsDist = FreqDist(bigrams)    #给出字典，二元词组及其对应的出现次数
print(bigramsDist[('Sir', 'Robin')])    #('Sir', 'Robin')出现的次数

fourgrams = ngrams(text6, 4)     #四元分词
#for fourgram in fourgrams:       #对分词结果进行迭代显示
#    if fourgram[0] == 'coconut':
#        print(fourgram)

print(fourgrams)

fourgramsDist = FreqDist(fourgrams)
print(fourgramsDist)
print(fourgramsDist[('father', 'smelt', 'of', 'elderberries')])  # 执行for loop后结果为0. 不执行为1



