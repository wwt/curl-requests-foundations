#!/bin/sh
# Step 2 - Get a list of your Webex Teams Rooms with the token
curl -iX GET --url https://webexapis.com/v1/rooms \
-H 'Authorization: Bearer '$WEBEX_TOKEN
