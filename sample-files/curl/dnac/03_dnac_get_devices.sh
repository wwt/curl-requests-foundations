#!/bin/sh
# Step 3 - Get a list of DNAC devices with the stored token
curl --url https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device \
-H 'Content-Type: application/json' -H 'X-Auth-Token:'$DNAC_TOKEN -ik
