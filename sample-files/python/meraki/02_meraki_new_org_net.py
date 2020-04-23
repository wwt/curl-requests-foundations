#!/usr/local/bin/python
new_network = {'name':'LA Office','type': 'switch','timeZone':'America/Los_Angeles'}
post_url = 'https://api.meraki.com/api/v0/organizations/549236/networks'
post_response = requests.post(post_url, headers=headers, json=new_network)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.text)
