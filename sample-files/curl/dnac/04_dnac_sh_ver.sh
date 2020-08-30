#!/bin/sh
# Step 4 - Run a 'show version' command on a device
curl -ikX POST \
-H 'Content-Type: application/json' -H 'X-Auth-Token:'$DNAC_TOKEN \
--url https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request \
--data-raw '{"name":"show ver","commands":["show ver"],"deviceUuids":["3e48558a-237a-4bca-8823-0580b88c6acf"]}'
