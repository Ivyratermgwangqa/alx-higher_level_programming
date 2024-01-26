# Python Networking Project

This repository contains a collection of Python scripts for various networking tasks. The tasks range from making HTTP requests, handling responses, to interacting with APIs.

## Table of Contents

1. [Introduction](#introduction)
2. [Tasks](#tasks)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Author](#author)
6. [License](#license)

## Introduction

The goal of this project is to demonstrate proficiency in handling network-related tasks using Python. Each script corresponds to a specific task and is designed to showcase different aspects of network programming.

## Tasks

### Task 0: What's my status? #0
- **Description:** This script fetches the status of the [Holberton intranet](https://alx-intranet.hbtn.io/status) using the `urllib` package.
- **Usage:** Execute `0-hbtn_status.py` to display information about the HTTP response.

### Task 1: Response header value #0
- **Description:** This script takes a URL, sends a request, and displays the value of the `X-Request-Id` variable in the header of the response using `urllib`.
- **Usage:** Execute `1-hbtn_header.py [URL]` to obtain and display the `X-Request-Id` value.

### Task 2: POST an email #0
- **Description:** This script sends a POST request to a URL with an email as a parameter and displays the response body using `urllib`.
- **Usage:** Execute `2-post_email.py [URL] [email]` to send a POST request with the specified email.

### Task 3: Error code #0
- **Description:** This script sends a request to a URL and displays the body of the response. It manages `urllib.error.HTTPError` exceptions and prints error codes when needed.
- **Usage:** Execute `3-error_code.py [URL]` to handle HTTP errors and display the response body.

### Task 4: What's my status? #1
- **Description:** This script fetches the status of the Holberton intranet using the `requests` package.
- **Usage:** Execute `4-hbtn_status.py` to obtain and display information about the HTTP response.

### Task 5: Response header value #1
- **Description:** This script takes a URL, sends a request, and displays the value of the `X-Request-Id` variable in the header of the response using the `requests` package.
- **Usage:** Execute `5-hbtn_header.py [URL]` to obtain and display the `X-Request-Id` value.

### Task 6: POST an email #1
- **Description:** This script sends a POST request to a URL with an email as a parameter and displays the response body using the `requests` package.
- **Usage:** Execute `6-post_email.py [URL] [email]` to send a POST request with the specified email.

### Task 7: Error code #1
- **Description:** This script sends a request to a URL and displays the body of the response. It prints error codes for HTTP status codes greater than or equal to 400.
- **Usage:** Execute `7-error_code.py [URL]` to handle HTTP errors and display the response body.

### Task 8: Search API
- **Description:** This script sends a POST request with a letter as a parameter to search for a user on a specified URL. It displays user information if found.
- **Usage:** Execute `8-json_api.py [letter]` to search for a user with the specified letter.

### Task 9: My GitHub!
- **Description:** This script uses Basic Authentication to access the GitHub API and displays the user id.
- **Usage:** Execute `10-my_github.py [username] [password]` to access GitHub information using your credentials.

### Task 10: Time for an interview! (Advanced)
- **Description:** This script lists the 10 most recent commits (from the most recent to oldest) of a specified GitHub repository and user.
- **Usage:** Execute `100-github_commits.py [repository] [owner]` to list the commits.

## Requirements

- Python 3.8.5
- Pycodestyle 2.8.*
- Requests library (for tasks using requests)

## Usage

- Each Python script is designed to be executed directly.
- Make sure to set execute permissions using `chmod +x filename.py`.
- Refer to each task's specific instructions for additional details on usage.

## Author

[Your Name]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

