#!/bin/sh
curl -X PUT -kib .cookie_jar -H 'X-XSRF-TOKEN: xsrf_token' \
-H 'Content-Type: application/json' \
--data-raw '{mode: "on", bannerDetail: "Welcome to vManage"}' \
--url https://sandboxsdwan.cisco.com:8443/dataservice/settings/configuration/banner
