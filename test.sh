#!/bin/bash

declare -a endpoints=("/store" "/search" "/count_tokens" "/split_tokens")

for endpoint in "${endpoints[@]}"; do
  response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "http://localhost:5000${endpoint}" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"messageId\":\"test_message_1\",\"text\":\"Test text\",\"n\":10}")
  if [ "$response" -eq 200 ]; then
    echo "Success: ${endpoint} returned a 200 status code."
  else
    echo "Error: ${endpoint} did not return a 200 status code. It returned a ${response} status code."
  fi
done
