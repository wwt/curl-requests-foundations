#!/usr/local/bin/python
import os, requests
from pprint import pprint
req_url = 'https://api.meraki.com/api/v0/organizations'
req_headers = {'X-Cisco-Meraki-API-Key':os.getenv('MERAKI_API_KEY')}
response = requests.get(req_url, headers=req_headers)
print(f'{response.status_code} {response.reason}\n')
pprint(response.json())
