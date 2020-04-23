#!/usr/local/bin/python
login_banner = "{'mode': 'on', 'bannerDetail': 'Welcome to vManage'}"
session.headers['Content-Type'] = 'application/json'
put_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/settings/configuration/banner'
put_response = session.put(put_url, json=login_banner)
print(f'{put_response.status_code} {put_response.reason}')
print(put_response.text)
