#!/bin/sh
# Step 4 - Run a 'show version' command on a device
curl -iX POST \
-H 'Content-Type: application/json' -H 'X-Auth-Token:'$DNAC_TOKEN \
--url https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request \
--data-raw '{"name":"show ver","commands":["show ver"],"deviceUuids":["183ed3e6-3472-405c-a1ce-26d07987a140"]}'
