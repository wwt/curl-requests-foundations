#!/bin/sh
# Step 6 - Get get the file ID from the 'show version' command runner task
curl --url https://sandboxdnac.cisco.com/dna/intent/api/v1/task/$DNAC_TASK \
-H 'Content-Type: application/json' -H 'X-Auth-Token:'$DNAC_TOKEN -i
