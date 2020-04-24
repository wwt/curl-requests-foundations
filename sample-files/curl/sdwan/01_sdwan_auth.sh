#!/bin/sh
# Step 1 - Authenticate & store token in a cookie file
curl -X POST -kic .cookie_jar \
--url https://sandboxsdwan.cisco.com:8443/dataservice/j_security_check \
--data-urlencode 'j_username=devnetuser' \
--data-urlencode 'j_password=Cisco123!'
