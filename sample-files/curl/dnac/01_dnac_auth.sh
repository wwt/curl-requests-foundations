#!/bin/sh
# Step 1 - Authenticate & retrieve a session token
curl -X POST -iu 'devnetuser:Cisco123!' -H 'Content-Type: application/json' \
--url https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token
