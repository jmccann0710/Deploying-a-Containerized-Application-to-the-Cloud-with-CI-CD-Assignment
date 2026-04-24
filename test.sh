#!/bin/bash

response=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:3000)

if [ "$response" == "200" ]; then
  echo "Application is running successfully!"
else
  echo "Application failed to start! HTTP Status: $response"
fi
