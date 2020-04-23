#!/usr/local/bin/python
from pprint import pprint
get_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/template/device'
get_response = session.get(get_url)
pprint(get_response.json()) # display all device templates
print() # blank line between output 
pprint(get_response.json()['data'][0]) #display the first template in the response
