#!/bin/sh
# Step 4 - Run a 'show version' command on a device
curl -iX POST \
-H 'Content-Type: application/json' -H 'X-Auth-Token:'$DNAC_TOKEN \
--url https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request \
--data-raw '{"name":"show ver","commands":["show ver"],"deviceUuids":["f16955ae-c349-47e9-8e8f-9b62104ab604"]}'
