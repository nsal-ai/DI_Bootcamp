import psycopg2 as p
from time import time
import requests

HOSTNAME = '127.0.0.1'
USERNAME = 'postgres'
PASSWORD = 'data123'
DATABASE = 'jokes'

connection = p.connect(
    host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

cursor = connection.cursor()



start = time()
for i in range(100):
    data = requests.get('https://api.chucknorris.io/jokes/random')
    data = data.json()
    joke = data['value']
    joke = joke.replace('"', '`')
    joke = joke.replace("'", '`')
    query = f"INSERT INTO all_jokes (joke) Values('{joke}')"
    cursor.execute(query)

connection.commit()

connection.close()

end = time()

print(end-start)