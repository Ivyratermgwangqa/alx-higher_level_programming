# ALX Higher Level Programming - Python Networking

This repository contains Bash and Python scripts for handling network-related tasks. The scripts use the `curl` command for making HTTP requests and cover various functionalities.

## Scripts and Descriptions

### 0-body_size.sh
This script takes a URL as input, sends a request, and displays the size of the response body in bytes.

### 1-body.sh
A script that sends a GET request to a URL and displays the body of the response for a 200 status code.

### 2-delete.sh
Sends a DELETE request to a URL and displays the body of the response.

### 3-methods.sh
Takes a URL and displays all HTTP methods the server will accept.

### 4-header.sh
Sends a GET request to a URL with a specific header and displays the body of the response.

### 5-post_params.sh
Sends a POST request to a URL with specified parameters and displays the body of the response.

### 6-peak.py
A Python script containing a function that finds a peak in a list of unsorted integers.

### 100-status_code.sh
A script that sends a request to a URL and displays only the status code of the response.

### 101-post_json.sh
Sends a JSON POST request to a URL and displays the body of the response.

### 102-catch_me.sh
A script that makes a request to a specific URL, causing the server to respond with a specific message.

## Requirements
- All scripts are tested on Ubuntu 20.04 LTS.
- Bash scripts are exactly 3 lines long and use `#!/bin/bash`.
- Python scripts are Python 3.8.5 compatible.
- Pycodestyle (PEP8) is used for Python code style.

## Usage
Ensure that the scripts have execution permissions (`chmod +x script_name.sh`) before running. Test the scripts in the provided sandbox environment using the web server running on port 5000.

Feel free to explore the scripts and adapt them as needed.
