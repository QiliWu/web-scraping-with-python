# -*- coding:utf-8 -*-
import requests

params = {'loginname':'石松子22', 'nloginpwd':'shisongzi2011'}
r = requests.post('https://passport.jd.com/new/login.aspx', data =params)

print(r.text)