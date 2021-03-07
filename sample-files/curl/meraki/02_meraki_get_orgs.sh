#!/bin/sh
# Step 2 - Get a list of Meraki organizations with the API token
curl -iLX GET --url https://api.meraki.com/api/v1/organizations \
-H X-Cisco-Meraki-API-Key:$MERAKI_TOKEN
