#!/usr/bin/env python

# Step 1 - Get a list of Meraki organizations with the API token
import requests, os
from pprint import pprint
headers = {'Content-Type':'application/json'}
headers.update({'X-Cisco-Meraki-API-Key':os.getenv('MERAKI_TOKEN')})
get_url = 'https://api.meraki.com/api/v1/organizations'
get_response = requests.get(get_url, headers=headers)
pprint(get_response.json()) # display all organizations
print() # blank line between output
print(get_response.json()[0]) #display the first organization in the response

# Step 2 - Create a new Meraki network
new_network = {'name':'LA Office','type': 'switch','timeZone':'America/Los_Angeles'}
post_url = 'https://api.meraki.com/api/v1/organizations/549236/networks'
post_response = requests.post(post_url, headers=headers, json=new_network)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.text)
