#!/bin/sh
# Step 4 - Get a list of Device Templates
curl -X GET -kib .cookie_jar -H 'X-XSRF-TOKEN:'$XSRF_TOKEN \
--url https://sandbox-sdwan-1.cisco.com/dataservice/template/device
