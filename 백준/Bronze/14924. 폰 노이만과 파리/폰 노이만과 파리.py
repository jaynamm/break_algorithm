import sys

s, t, d = map(int, sys.stdin.readline().split())

print(d // (s * 2) * t)
