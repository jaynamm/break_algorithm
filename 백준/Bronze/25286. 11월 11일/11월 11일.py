import sys
import datetime

t = int(sys.stdin.readline())

for _ in range(t):
    y, m = map(int, sys.stdin.readline().split())

    print((datetime.datetime(y, m, m) - datetime.timedelta(days=m)).strftime('%Y %-m %d'))