#!/bin/bash
# Script that sends a JSON POST request to a URL with the contents of a file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
