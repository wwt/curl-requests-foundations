#!/usr/local/bin/python
token = {'X-Auth-Token':response.json()['Token']}
headers.update(token)
print(headers) # display the updated headers
