#!/usr/local/bin/python

# Step 1 - Authenticate & retreive a session token
import requests
requests.packages.urllib3.disable_warnings() # disable insecure SSL warnings
auth_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/j_security_check'
auth_data = {'j_username': 'devnetuser', 'j_password': 'Cisco123!'}
session = requests.session()
session.verify = False # permit self-signed certificates
session.post(auth_url, data=auth_data)
print(session.cookies['JSESSIONID']) # display the session token

# Step 2 - Get an XSRF token
xsrf_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/client/token'
xsrf_response = session.get(xsrf_url)
session.headers['X-XSRF-TOKEN'] = xsrf_response.content
print(f'{xsrf_response.status_code} {xsrf_response.reason}')
print(session.headers['X-XSRF-TOKEN'])

# Step 3 - Get a list of Device Templates
from pprint import pprint
get_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/template/device'
get_response = session.get(get_url)
pprint(get_response.json()) # display all device templates
print() # blank line between output 
pprint(get_response.json()['data'][0]) #display the first template in the response

# Step 4 - Enable the vManage Login Banner
login_banner = "{'mode': 'on', 'bannerDetail': 'Welcome to vManage'}"
session.headers['Content-Type'] = 'application/json'
put_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/settings/configuration/banner'
put_response = session.put(put_url, json=login_banner)
print(f'{put_response.status_code} {put_response.reason}')
print(put_response.text)
