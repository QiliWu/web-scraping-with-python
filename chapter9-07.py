import requests
from requests.auth import HTTPBasicAuth, AuthBase

auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url='http://pythonscraping.come/pages/auth/login.php', auth=auth)
print(r.text)