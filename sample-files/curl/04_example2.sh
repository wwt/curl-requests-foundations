#!/bin/sh
curl -X POST --url https://jsonplaceholder.typicode.com/posts \
-H 'Content-Type: application/json' \
-id '{"id":101, "userId":1, "title":"Hello", "body":"Hello World!"}'
