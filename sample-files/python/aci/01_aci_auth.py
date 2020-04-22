#!/usr/local/bin/python
import requests
requests.packages.urllib3.disable_warnings() # disable insecure SSL warnings
auth_url = 'https://sandboxapicdc.cisco.com/api/aaaLogin.json'
auth_data = {'aaaUser':{'attributes':{'name':'admin', 'pwd':'ciscopsdt'}}}
session = requests.session()
session.verify = False # permit self-signed certificates
response = session.post(auth_url, json=auth_data)
print(response.cookies) # option 1 to display the session token
print() # blank line between options
print(response.json()) # option 2 to display the session token
