#!/bin/sh
curl -X GET -kib .cookie_jar -H 'X-XSRF-TOKEN: xsrf_token' \
--url https://sandboxsdwan.cisco.com:8443/dataservice/template/device
