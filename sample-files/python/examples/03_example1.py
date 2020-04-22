#!/usr/local/bin/python
import requests
req_url = 'https://jsonplaceholder.typicode.com/posts/1'
req_headers = {'Content-Type':'application/json'}
response = requests.get(req_url, headers=req_headers)
print(f'{response.status_code} {response.reason}')
print(response.text)
