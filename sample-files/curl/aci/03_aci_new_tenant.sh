#!/bin/sh
curl -X POST --url https://sandboxapicdc.cisco.com/api/mo/uni.json \
--data-raw '{"fvTenant":{"attributes":{"name":"my_new_tenant"}}}' \
-kib .cookie_jar
