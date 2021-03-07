#!/usr/bin/env python

# Step 1
import requests
req_url = 'https://jsonplaceholder.typicode.com/posts/1'
req_headers = {'Content-Type':'application/json'}
response = requests.get(req_url, headers=req_headers)
print(f'{response.status_code} {response.reason}')
print(response.text)

# Step 2
req_url = 'https://jsonplaceholder.typicode.com/posts'
req_headers = {'Content-Type':'application/json'}
req_body = {"id":101, "userId":1, "title":"Hello", "body":"Hello World!"}
response = requests.post(req_url, headers=req_headers, json=req_body)
print(f'{response.status_code} {response.reason}\n')
print(response.text)

# Step 3
import os
req_url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
req_auth = (os.getenv('DNAC_USER'), os.getenv('DNAC_PW'))
response = requests.post(req_url, auth=req_auth)
print(f'{response.status_code} {response.reason}\n')
print(f'{response.headers}\n{response.text}')

# Step 4
from pprint import pprint
req_url = 'https://api.meraki.com/api/v1/organizations'
req_headers = {'X-Cisco-Meraki-API-Key':os.getenv('MERAKI_TOKEN')}
response = requests.get(req_url, headers=req_headers)
print(f'{response.status_code} {response.reason}\n')
pprint(response.json())
