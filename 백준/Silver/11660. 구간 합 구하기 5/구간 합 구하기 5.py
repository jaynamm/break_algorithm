import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    if x1 == x2 and y1 == y2:
        result = graph[x1-1][y1-1]
    else:
        if x1 == 1:
            result = dp[x2][y2] - dp[x2][y1-1]
        elif y1 == 1:
            result = dp[x2][y2] - dp[x1-1][y2]
        else:
            result = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1])
            
    print(result)