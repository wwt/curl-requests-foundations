#!/usr/local/bin/python
import requests
auth_url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
headers = {'Content-Type':'application/json'}
auth_data = ('devnetuser', 'Cisco123!')
response = requests.post(auth_url, headers=headers, auth=auth_data)
print(response.json()) # display the session token
