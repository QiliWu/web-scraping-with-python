#using json.loads() to decode the string text

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    print('aa'+response)
    print((type(response)))    #response is a string
    responseJson = json.loads(response)   #return a dict
    print(type(responseJson))
    return responseJson

print(getCountry('50.78.253.58'))
print(getCountry('202.116.83.180'))