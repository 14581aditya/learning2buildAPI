import requests
import json

response = requests.get("http://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow")

for data in response.json()['items']:
    if data['answer_count']:
        print(data['title'])
        print(data['link'])
    else:
        print("skipped")
    print()




