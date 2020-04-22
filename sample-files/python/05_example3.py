#!/usr/local/bin/python
import os, requests
req_url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
req_auth = (os.getenv('DNAC_USER'), os.getenv('DNAC_PW'))
response = requests.post(req_url, auth=req_auth)
print(f'{response.status_code} {response.reason}\n')
print(f'{response.headers}\n{response.text}')
