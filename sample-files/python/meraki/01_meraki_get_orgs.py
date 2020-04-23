#!/usr/local/bin/python
import requests, os
from pprint import pprint
headers = {'Content-Type':'application/json'}
headers.update({'X-Cisco-Meraki-API-Key':os.getenv('MERAKI_TOKEN')})
get_url = 'https://api.meraki.com/api/v0/organizations'
get_response = requests.get(get_url, headers=headers)
pprint(get_response.json()) # display all organizations
print() # blank line between output 
print(get_response.json()[0]) #display the first organization in the response
