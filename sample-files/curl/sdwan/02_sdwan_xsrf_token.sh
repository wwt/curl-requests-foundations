#!/bin/sh
# Step 2 - Get an XSRF token
curl -X GET --url https://sandboxsdwan.cisco.com:8443/dataservice/client/token \
-kib .cookie_jar
