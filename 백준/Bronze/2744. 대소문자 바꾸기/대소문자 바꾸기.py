import sys

s = sys.stdin.readline().strip()
print("".join([s[i].lower() if s[i].isupper() else s[i].upper() for i in range(len(s))]))