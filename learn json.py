import json

obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)

#the results are almost same, but the tuple turn to be list,and the whole result is a string
print(obj)    #[[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
print(type(obj))     #<class 'list'>
print(encodedjson)    #[[1, 2, 3], 123, 123.123, "abc", {"key1": [1, 2, 3], "key2": [4, 5, 6]}]
print(type(encodedjson))   #<class 'str'>!!!!


#json.dumps() return a str object:encodedjson, in order to decode and get the raw data, we need
#to use json.loads()

decodejson = json.loads(encodedjson)
print(type(decodejson))   #<class 'list'>
print(decodejson)     #[[1, 2, 3], 123, 123.123, 'abc', {'key1': [1, 2, 3], 'key2': [4, 5, 6]}]
print(decodejson[4])      #{'key1': [1, 2, 3], 'key2': [4, 5, 6]}

