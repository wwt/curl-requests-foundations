#!/bin/sh
curl -iLX GET --url https://api.meraki.com/api/v0/organizations \
-H X-Cisco-Meraki-API-Key:$MERAKI_TOKEN
