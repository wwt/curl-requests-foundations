#!/usr/local/bin/python
token = session.cookies['APIC-cookie'] # option1
token = response.json()['imdata'][0]['aaaLogin']['attributes']['token'] # option2
session_cookie = {'APIC-Cookie':token}
print(session_cookie)
