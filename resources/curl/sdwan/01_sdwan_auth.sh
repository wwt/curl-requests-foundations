#!/bin/sh
# Step 1 - Authenticate & store token in a cookie file
curl -X POST -kic .cookie_jar \
--url https://sandbox-sdwan-1.cisco.com/dataservice/j_security_check \
--data-urlencode 'j_username=devnetuser' \
--data-urlencode 'j_password=RG!_Yw919_83'
