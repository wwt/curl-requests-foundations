#!/bin/sh
# Step 5 - Enable the vManage Login Banner
curl -X PUT -kib .cookie_jar -H 'X-XSRF-TOKEN:'$XSRF_TOKEN \
-H 'Content-Type: application/json' \
--data-raw '{mode: "on", bannerDetail: "Welcome to vManage"}' \
--url https://sandboxsdwan.cisco.com:8443/dataservice/settings/configuration/banner
