# -*- coding:utf-8 -*-
import requests
#失败
params = {'loginname':'******', 'nloginpwd':'*******'}
r = requests.post('https://passport.jd.com/new/login', data =params)

print(r.text)