import requests 
import json
from operator import itemgetter
import urllib3

url = ' https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status Code: {r.status_code}')


    


submission_ids = r.json()
readable_file = 'readable_hn_data.json'

with open(readable_file, 'w') as f:
    json.dump(submission_ids, f, indent=4)


submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:5]:
    url = f'https://hacker-news.firebasio.com/v0/item/{submission_id}.json?print=pretty'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    response_dict = r.json()


    submission_dict = {
        'title': response_dict['title'],
        'url': f'http://news.ycombinator.com/item?id={submission_id}',
        'descendants' : response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('descendants'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['url']}")
    print(f"Comments: {submission_dict['descendants']}")


