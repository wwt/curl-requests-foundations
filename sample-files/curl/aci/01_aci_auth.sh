#!/bin/sh
# Step 1 - Authenticate & store token in a cookie file
curl -X POST --url https://sandboxapicdc.cisco.com/api/aaaLogin.json \
--data-raw '{"aaaUser":{"attributes":{"name":"admin","pwd":"ciscopsdt"}}}' \
-kic .cookie_jar
