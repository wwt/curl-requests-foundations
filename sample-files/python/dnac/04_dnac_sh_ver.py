#!/usr/local/bin/python
cli_commands = {'name':'show ver','commands':['show ver'],'deviceUuids':['3e48558a-237a-4bca-8823-0580b88c6acf']}
post_url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request'
post_response = requests.post(post_url, headers=headers, json=cli_commands)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.json())
