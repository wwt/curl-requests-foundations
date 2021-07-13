#!/bin/sh
# Step 8 - Get get the file ID from the 'show version' command runner task
curl --url https://sandboxdnac.cisco.com/dna/intent/api/v1/file/$DNAC_FILE \
-H 'Content-Type: application/json' -H 'X-Auth-Token:'$DNAC_TOKEN -i
