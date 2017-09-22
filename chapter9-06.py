import requests

session = requests.session()
params = {'username':'qiliwu', 'password':'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data = params)
print(s.text)
print('Cookie is set to: ')
print(s.cookies.get_dict())
print('-'*30)
print('Going to profile page...')
#s = session.post('http://pythonscraping.com/pages/cookies/profile.php')
s = requests.post('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)