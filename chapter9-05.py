import requests
params = {'username':'qiliwu', 'password':'password'}
#  POST
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=params)
print(r.text)
print("Cookie is set to:")
print(r.cookies.get_dict())
print('-'*20)
print('Going to profile page...')
#GET， with cookies
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)