#!/usr/bin/python3
import sys
import re
import signal

num = 0
size = 0
lists = []
codes = [200, 301, 400, 401, 403, 404, 405, 500]
code_counts = {code: 0 for code in codes}


def handle(sig, frame):
    """Handle keyboard interrupt (Ctrl+C)"""
    if sig == signal.SIGINT:
        print_summary()


def print_summary():
    """Print the summary of file size and code counts"""
    print("File size: {}".format(size))
    for code in codes:
        if code_counts[code] > 0:
            print("{}: {}".format(code, code_counts[code]))


signal.signal(signal.SIGINT, handle)

regex = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
)

while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()

    match = re.match(regex, line)
    if not match:
        continue

    file_size = int(match.group(4))
    size += file_size

    status_code = int(match.group(3))
    if status_code in code_counts:
        code_counts[status_code] += 1

    num += 1

    if num == 10:
        print_summary()
        num = 0
