import requests
import json

url = 'http://localhost:8008'

payload = json.dumps({'first': '1', 'second': '2'})
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=payload, headers=headers)
