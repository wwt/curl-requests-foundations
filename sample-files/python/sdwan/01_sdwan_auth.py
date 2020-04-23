#!/usr/local/bin/python
import requests
requests.packages.urllib3.disable_warnings() # disable insecure SSL warnings
auth_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/j_security_check'
auth_data = {'j_username': 'devnetuser', 'j_password': 'Cisco123!'}
session = requests.session()
session.verify = False # permit self-signed certificates
session.post(auth_url, data=auth_data)
print(session.cookies['JSESSIONID']) # display the session token
