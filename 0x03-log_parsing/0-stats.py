#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys

# Initialize variables to hold metrics
total_size = 0
status_counts = {}

# Loop over stdin, processing input line by line
for i, line in enumerate(sys.stdin, 1):
    try:
        # Parse input line to extract status code and file size
        parts = line.split()
        status_code = int(parts[8])
        file_size = int(parts[9])

        # Update total file size
        total_size += file_size

        # Update status code counts
        if status_code not in status_counts:
            status_counts[status_code] = 0
        status_counts[status_code] += 1

        # Print metrics every 10 lines or on keyboard interrupt
        if i % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_counts.keys()):
                print(f"{status_code}: {status_counts[status_code]}")
            print()

    except KeyboardInterrupt:
        # Print metrics on keyboard interrupt
        print("Total file size:", total_size)
        for status_code in sorted(status_counts.keys()):
            print(f"{status_code}: {status_counts[status_code]}")
        sys.exit(0)

    except (ValueError, IndexError):
        # Skip line if format is invalid
        continue
