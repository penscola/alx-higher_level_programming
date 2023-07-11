#!/usr/bin/python3
"""101-stats.py - reads stdin line by line and computes metrics
"""
import sys

if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    total_size = 0
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            total_size += int(data[-1])
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
            if count % 10 == 0:
                print("File size: {:d}".format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value > 0:
                        print("{:s}: {:d}".format(key, value))
    except KeyboardInterrupt:
        print("File size: {:d}".format(total_size))
        for key, value in sorted(status_codes.items()):
            if value > 0:
                print("{:s}: {:d}".format(key, value))
        raise
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))
