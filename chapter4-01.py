#using json.loads() to decode the string text

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    print(response)
    print((type(response)))    #response is a string
    responseJson = json.loads(response)   #return a dict
    print(type(responseJson))

    response2 = urlopen('http://freegeoip.net/json/' + ipAddress).read()
    print(response2)
    print(type(response2))   # bytes
    responseJson2 = json.loads(response2)

    responseJson3 = json.dumps(response)   # str type
    #responseJson4 = json.dumps(response2)  # error  , bytes is not JSON serializable
    print('22', type(responseJson2))
    print('33', type(responseJson3))
    return responseJson

print(getCountry('50.78.253.58'))
print(getCountry('202.116.83.180'))