import requests

params = {'firstname': 'Qili', 'lastname': 'Wu'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=params)

print(r.text)