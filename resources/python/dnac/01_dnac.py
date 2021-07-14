#!/usr/bin/env python

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
cli_commands = {'name':'show ver','commands':['show ver'],'deviceUuids':['f16955ae-c349-47e9-8e8f-9b62104ab604']}
post_url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request'
post_response = requests.post(post_url, headers=headers, json=cli_commands)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.json())

# Step 5 - If DNAC returns a '202 Accepted' for the previous task, check the status of the request and get the file ID
task_id = post_response.json()['response']['taskId']
get_url = f'https://sandboxdnac.cisco.com/dna/intent/api/v1/task/{task_id}'
get_response = requests.get(get_url, headers=headers)
print(f'{get_response.status_code} {get_response.reason}')
print(get_response.json())
file = get_response.json()['response']['progress']

# Step 6 - # DNAC returns a string object which looks like a dictionary
# Remediation option #1 - use the JSON module to convert the string to a dictionary
import json
file = get_response.json()['response']['progress']
file_id_dict = json.loads(file)
file_id = file_id_dict['fileId']
# Remediation option #2 - use regex to parse the file ID
import re
search_pattern = re.compile(r'[a-f0-9-]+(?="})')
match = search_pattern.search(file)
file_id = match.group(0)

# Step 7 - If DNAC returns a '200 OK' for the previous command, get the file contents
get_url = f'https://sandboxdnac.cisco.com/dna/intent/api/v1/file/{file_id}'
get_response = requests.get(get_url, headers=headers)
print(f'{get_response.status_code} {get_response.reason}')
print(get_response.json())
