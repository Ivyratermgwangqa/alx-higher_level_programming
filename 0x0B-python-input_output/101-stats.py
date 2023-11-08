#!/usr/bin/python3

"""
This script reads lines from standard input and calculates statistics about the lines, including the total file size and counts of different status codes.

The script runs indefinitely, continuously reading lines until it receives a KeyboardInterrupt (usually triggered by pressing Ctrl+C).

Statistics are printed to the console after processing every 10 lines.

Usage: You can use this script to analyze log files or other text-based data to calculate statistics on file sizes and status codes.

"""

if __name__ == "__main__":
    import sys

    # Initialize variables to store statistics
    size = 0  # Total file size
    statuscd = {}  # Count of different status codes

    while True:
        try:
            counter = 0
            for line in sys.stdin:
                # Split each line into words
                line = line.split()

                # Update total file size
                size += int(line[8])

                # Update status code count
                if statuscd.get(line[7], -1) == -1:
                    statuscd[line[7]] = 1
                else:
                    statuscd[line[7]] += 1

                # After processing 10 lines, break out of the loop
                if counter == 10:
                    break
                counter += 1

        except KeyboardInterrupt:
            # Exit gracefully when a KeyboardInterrupt is received (e.g., Ctrl+C)
            exit()
        finally:
            # Print the calculated statistics
            print("File size: {}".format(size))
            for key in sorted(statuscd):
                print("{}: {}".format(key, statuscd[key]))
