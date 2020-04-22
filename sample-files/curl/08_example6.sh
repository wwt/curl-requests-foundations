#!/bin/bash
export MERAKI_TOKEN=6bec40cf957de430a6f1f2baa056b99a4fac9ea0

curl --url https://api.meraki.com/api/v0/organizations \
-H X-Cisco-Meraki-API-Key:$MERAKI_TOKEN \
-H 'Accept: */*' -i \
-L
