#!/bin/sh
# Step 2 - Get a list of APIC Tenants with the stored token
curl --url https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json \
-kib .cookie_jar
