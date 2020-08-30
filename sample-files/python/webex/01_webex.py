#!/usr/bin/env python

# Step 1 - Get a list of your Webex Teams Rooms with the token
import requests, os
from pprint import pprint
token = os.getenv('WEBEX_TOKEN')
headers = {'Content-Type':'application/json','Authorization':f'Bearer {token}'}
get_url = 'https://webexapis.com/v1/rooms'
get_response = requests.get(get_url, headers=headers)
pprint(get_response.json()) # display all rooms
print() # blank line between output
pprint(get_response.json()['items'][0]) # display the first room in the response

# Step 2 - Create a new Webex Teams Room
new_room = {'title':'New Python Room'}
post_url = 'https://webexapis.com/v1/rooms'
post_response = requests.post(post_url, headers=headers, json=new_room)
print(f'{post_response.status_code} {post_response.reason}')
pprint(post_response.json())

# Step 3 - Post a message to the new Webex Teams Room
new_msg = {'roomId':post_response.json()['id'],'text':'Hello from Python'}
msg_url = 'https://webexapis.com/v1/messages'
msg_response = requests.post(msg_url, headers=headers, json=new_msg)
print(f'{msg_response.status_code} {msg_response.reason}')
pprint(msg_response.json())
