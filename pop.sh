#!/bin/bash
for i in {1..25}
do
   RANDOM_TEXT="Random text number $RANDOM"
   curl -X POST "http://localhost:5000/store" \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        -d "{\"messageId\":\"test_message_$i\",\"text\":\"$RANDOM_TEXT\"}"
done
