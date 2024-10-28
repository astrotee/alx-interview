#!/usr/bin/python3
"log parsing"
import signal
import sys
import re


count = 0
file_size = 0
status_count = {c: 0 for c in ['200', '301', '400', '401',
                               '403', '404', '405', '500']}
pattern = (
    r'(?P<ip>(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}'
    r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?))'
    r' - \[(?P<date>.+)\] "GET /projects/260 HTTP/1.1"'
    r' (?P<status>200|301|400|401|403|404|405|500) (?P<size>\d+)'
)


def report():
    "print a summary of the logs"
    global file_size
    global status_count
    print(f'File size: {file_size}')
    for code, count in status_count.items():
        if count == 0:
            continue
        print(f'{code}: {count}')


def handler(signum, frame):
    "SIGINT handler"
    report()
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, handler)


if __name__ == "__main__":
    pattern = re.compile(pattern)

    for line in sys.stdin:
        match = pattern.fullmatch(line.strip())
        if not match:
            continue
        count += 1
        file_size += int(match.groupdict()['size'])
        status_count[match.groupdict()['status']] += 1
        if count == 10:
            report()
            count = 0
    if 10 - count > 0:
        report()
