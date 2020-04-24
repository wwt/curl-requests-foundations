#!/usr/local/bin/python

# Step 1 - Authenticate & retreive a session token
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

# Step 2 - Store the session token in a variable
token = session.cookies['APIC-cookie'] # option1
token = response.json()['imdata'][0]['aaaLogin']['attributes']['token'] # option2
session_cookie = {'APIC-Cookie':token}
print(session_cookie)

# Step 3 - Get a list of APIC Tenants with the stored token
from pprint import pprint
get_url = 'https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json'
get_response = session.get(get_url, cookies=session_cookie)
pprint(get_response.json()) # display all tenants
print() # blank line between output
pprint(get_response.json()['imdata'][0]) #display the first tenant in the response

# Step 4 - Create a new tenant
new_tenant = {'fvTenant':{'attributes':{'name':'my_new_tenant'}}}
post_url = 'https://sandboxapicdc.cisco.com/api/mo/uni.json'
post_response = session.post(post_url, json=new_tenant, cookies=session_cookie)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.json())
