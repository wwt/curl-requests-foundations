#!/bin/sh
# Create environment variables for DNAC authentication
export DNAC_USER=devnetuser
export DNAC_PW=Cisco123!

curl -X POST --url https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token \
-u $DNAC_USER:$DNAC_PW \
-vo ~/token.txt
