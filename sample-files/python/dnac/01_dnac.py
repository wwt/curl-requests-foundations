#!/usr/local/bin/python

# Step 1 - Authenticate & retrieve a session token
import requests
auth_url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
headers = {'Content-Type':'application/json'}
auth_data = ('devnetuser', 'Cisco123!')
response = requests.post(auth_url, headers=headers, auth=auth_data)
print(response.json()) # display the session token

# Step 2 - Store the token in a variable
token = {'X-Auth-Token':response.json()['Token']}
headers.update(token)
print(headers) # display the updated headers

# Step 3 - Get a list of DNAC devices with the stored token
from pprint import pprint
get_url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
get_response = requests.get(get_url, headers=headers)
pprint(get_response.json()) # display all devices
print() # blank line between output
pprint(get_response.json()['response'][0]) #display the first device in the response

# Step 4 - Run a 'show version' command on a device
cli_commands = {'name':'show ver','commands':['show ver'],'deviceUuids':['3e48558a-237a-4bca-8823-0580b88c6acf']}
post_url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request'
post_response = requests.post(post_url, headers=headers, json=cli_commands)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.json())
