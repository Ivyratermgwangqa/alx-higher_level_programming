#!/usr/bin/python3
"""
Module: log_parser
This module defines a log parsing script that reads log lines.

The script reads log lines from standard input.
"""


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}

    while True:
        try:
            counter = 0
            for line in sys.stdin:
                line = line.split()

                size += int(line[8])
                if line[7] in status_codes:
                    status_codes[line[7]] += 1
                else:
                    status_codes[line[7]] = 1

                if counter == 10:
                    break
                counter += 1

        except KeyboardInterrupt:
            exit()
        finally:
            print("File size: {}".format(size))
            for key in sorted(status_codes):
                print("{}: {}".format(key, status_codes[key]))
