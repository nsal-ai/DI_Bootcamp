
# retrieving data from API using python bash terminal
# response 200 is good
# data odject used to extract key value 'value' from json dictionary

$ python
Python 3.8.9 (tags/v3.8.9:a743f81, Apr  2 2021, 11:10:41) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> request.get('https://api.chucknorris.io/jokes/random')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'request' is not defined
>>> requests.get('https://api.chucknorris.io/jokes/random')
<Response [200]>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'requests']
>>> data = requests.get('https://api.chucknorris.io/jokes/random')
>>> data.json
<bound method Response.json of <Response [200]>>
>>> data.json()
{'categories': [], 'created_at': '2020-01-05 13:42:27.496799', 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': 'OklJ3oTeREetkVkrrkyIOg', 'updated_at': '2020-01-05 13:42:27.496799', 'url': 'https://api.chucknorris.io/jokes/OklJ3oTeREetkVkrrkyIOg', 'value': "It's the assholes like John West that Chuck Norris brutally roundhouse kicks, that makes Chuck Norris the best."}
>>> data.json()['value']
"It's the assholes like John West that Chuck Norris brutally roundhouse kicks, that makes Chuck Norris the best."
>>> data.json()['value']
"It's the assholes like John West that Chuck Norris brutally roundhouse kicks, that makes Chuck Norris the best."
>>> data.json()['value']
"It's the assholes like John West that Chuck Norris brutally roundhouse kicks, that makes Chuck Norris the best."
>>> data = requests.get('https://api.chucknorris.io/jokes/random')
>>> data.json()
{'categories': [], 'created_at': '2020-01-05 13:42:23.880601', 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': 'QBz3siqtRuCw-oJKg-gJPA', 'updated_at': '2020-01-05 13:42:23.880601', 'url': 'https://api.chucknorris.io/jokes/QBz3siqtRuCw-oJKg-gJPA', 'value': 'Five Finger Death Punch and Twelve Foot Ninja are rock bands named after the way Chuck Norris killed a giant ninja.'}
>>> data.json()['value']
'Five Finger Death Punch and Twelve Foot Ninja are rock bands named after the way Chuck Norris killed a giant ninja.'
>>> exit()

