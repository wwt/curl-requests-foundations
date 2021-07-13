#!/bin/sh
# Step 4 - Get a list of Device Templates
curl -X GET -kib .cookie_jar -H 'X-XSRF-TOKEN:'$XSRF_TOKEN \
--url https://sandboxsdwan.cisco.com:8443/dataservice/template/device
