#!/usr/local/bin/python
from pprint import pprint
get_url = 'https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json'
get_response = session.get(get_url, cookies=session_cookie)
pprint(get_response.json()) # display all tenants
print() # blank line between output
pprint(get_response.json()['imdata'][0]) #display the first tenant in the response
