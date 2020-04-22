#!/bin/sh
curl -iLX POST \
--url https://api.meraki.com/api/v0/organizations/549236/networks \
-H 'Content-Type: application/json' -H 'X-Cisco-Meraki-API-Key:'$MERAKI_TOKEN \
--data-raw '{"name":"LA Office","type": "switch","timeZone":"America/Los_Angeles"}'
