#!/bin/sh
curl -X POST --url https://sandboxapicdc.cisco.com/api/aaaLogin.json \
--data-raw '{"aaaUser":{"attributes":{"name":"admin","pwd":"ciscopsdt"}}}' \
-kic .cookie_jar
