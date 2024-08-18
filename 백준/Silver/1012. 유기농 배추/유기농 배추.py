import sys
from collections import deque

def bfs(i, j):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(i, j)])
    visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
    
        for k in range(4):    
            if 0 <= x + dx[k] < n and 0 <= y + dy[k] < m and land[x + dx[k]][y + dy[k]] == 1 and not visited[x + dx[k]][y + dy[k]]:
                visited[x + dx[k]][y + dy[k]] = True
                queue.append((x + dx[k], y + dy[k]))
        
t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    x, y = [], []
    
    for _ in range(k):    
        x_num, y_num = map(int, sys.stdin.readline().split())
        x.append(x_num)
        y.append(y_num)

    land = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for x, y in zip(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            continue

        land[y][x] = 1

    bug = 0
        
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            else:
                if land[i][j] == 1:
                    bfs(i, j)
                    bug += 1
                
    print(bug)