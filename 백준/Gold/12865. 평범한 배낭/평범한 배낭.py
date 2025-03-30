import sys

n, k = map(int, sys.stdin.readline().split())

obj = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (k + 1)

for i in range(n):
    w = obj[i][0]
    v = obj[i][1]

    if w > k:
        continue

    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(max(dp))
