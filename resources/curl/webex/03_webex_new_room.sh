#!/bin/sh
# Step 3 - Create a new Webex Teams Room
curl -X POST --url https://webexapis.com/v1/rooms \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer '$WEBEX_TOKEN \
--data-raw '{"title":"New cURL Room"}'
