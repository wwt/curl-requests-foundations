#!/usr/local/bin/python
from pprint import pprint
get_url = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
get_response = requests.get(get_url, headers=headers)
pprint(get_response.json()) # display all devices
print() # blank line between output
pprint(get_response.json()['response'][0]) #display the first device in the response
