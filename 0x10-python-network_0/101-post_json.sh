#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response
filename=$2
if [ -f "$filename" ]; then
    curl -sX POST -H "Content-Type: application/json" -d @"$filename" "$1"
else
    echo "Not a valid JSON"
fi
