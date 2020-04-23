#!/usr/local/bin/python
xsrf_url = 'https://sandboxsdwan.cisco.com:8443/dataservice/client/token'
xsrf_response = session.get(xsrf_url)
session.headers['X-XSRF-TOKEN'] = xsrf_response.content
print(f'{xsrf_response.status_code} {xsrf_response.reason}')
print(session.headers['X-XSRF-TOKEN'])
