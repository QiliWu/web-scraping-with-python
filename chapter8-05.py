from nltk import FreqDist
from nltk.book import *
from nltk import bigrams
from nltk import ngrams

fdist = FreqDist(text6)
print(fdist.most_common(10))
print(type(fdist))
print(fdist['Grail'])

bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
print(bigramsDist[('Sir', 'Robin')])

fourgrams = ngrams(text6, 4)
#for fourgram in fourgrams:
#    if fourgram[0] == 'coconut':
#        print(fourgram)

print(fourgrams)

fourgramsDist = FreqDist(fourgrams)
print(fourgramsDist)
print(fourgramsDist[('father', 'smelt', 'of', 'elderberries')])  # 执行for loop后结果为0. 不执行为1



