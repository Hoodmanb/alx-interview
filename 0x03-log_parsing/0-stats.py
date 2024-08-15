##!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys
import re
import signal


total_size = 0
status_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

regex = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
)


def print_metrics():
    """Function to print file size and status code metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handle_interrupt(sig, frame):
    """Handle keyboard interruption (CTRL + C) to print metrics and exit."""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        match = re.match(regex, line.strip())
        if match:
            total_size += int(match.group(4))
            status_code = int(match.group(3))
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
print_metrics()
regex = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
)


def print_metrics():
    """Function to print file size and status code metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def handle_interrupt(sig, frame):
    """Handle keyboard interruption (CTRL + C) to print metrics and exit."""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)
try:
    for line in sys.stdin:
        match = re.match(regex, line.strip())
        if match:
            total_size += int(match.group(4))
            status_code = int(match.group(3))
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_metrics()

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
print_metrics()
