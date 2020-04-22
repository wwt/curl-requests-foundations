#!/usr/local/bin/python
import requests
req_url = 'https://jsonplaceholder.typicode.com/posts'
req_headers = {'Content-Type':'application/json'}
req_body = {"id":101, "userId":1, "title":"Hello", "body":"Hello World!"}
response = requests.post(req_url, headers=req_headers, json=req_body)
print(f'{response.status_code} {response.reason}\n')
print(response.text)
