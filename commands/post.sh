#!/bin/bash

APP_PORT=${PORT:-3000}

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{	"level": "error",	"message": "Failed to connect to DB", "resourceId": "server-1234",	"timestamp": "2023-09-15T08:00:00Z","traceId": "abc-xyz-124", "spanId": "span-456", "commit": "5e5342f", "metadata": {"parentResourceId": "server-0987"}}' \
  http://0.0.0.0:${APP_PORT}/api/v1/insert