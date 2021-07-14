#!/bin/sh
# Step 2 - Get an XSRF token
curl -X GET --url https://sandbox-sdwan-1.cisco.com/dataservice/client/token \
-kib .cookie_jar
