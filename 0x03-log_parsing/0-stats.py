#!/usr/bin/python3
import sys
import re
import signal


def handle(sig, frame):
    if sig == signal.SIGINT:
        return True
    return False


regex = (
    r'(\d{1,3}(?:\.\d{1,3}){3}) - \[(.*?)\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'
)
num = 0
size = 0
lists = []
# a = 0

while True:
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()
    match = re.match(regex, line)
    if not match:
        continue
    string = line.split()
    size += int(string[-1])
    lists.append(string[-2])
    num += 1
    signals = signal.signal(signal.SIGINT, handle)
    if num == 10 or signals:
        print("Filse size: {}".format(size))
        codes = [200, 301, 400, 401, 403, 404, 405, 500]
        for c in codes:
            sortedList = sorted(lists)
            counts = sortedList.count(str(c))
            if counts:
                print('{}: {}'.format(c, counts))
            continue
