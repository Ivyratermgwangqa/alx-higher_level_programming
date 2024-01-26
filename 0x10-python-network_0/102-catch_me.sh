#!/bin/bash
# Makes a request to a specific URL causing the server to respond with a specific message
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
