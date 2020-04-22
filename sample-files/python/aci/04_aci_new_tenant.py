#!/usr/local/bin/python
new_tenant = {'fvTenant':{'attributes':{'name':'my_new_tenant'}}}
post_url = 'https://sandboxapicdc.cisco.com/api/mo/uni.json'
post_response = session.post(post_url, json=new_tenant, cookies=session_cookie)
print(f'{post_response.status_code} {post_response.reason}')
print(post_response.json())
