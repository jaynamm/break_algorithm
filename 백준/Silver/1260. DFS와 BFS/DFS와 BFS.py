from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
    

def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")
    
    for i in range(1, n+1):
        if not dfs_visited[i] and graph[v][i] == 1:
            dfs(i)

            
def bfs(v):
    bfs_visited[v] = True
    queue = deque()
    queue.append(v)
    
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        
        for i in range(1, n+1):
            if not bfs_visited[i] and graph[x][i] == 1:
                queue.append(i)
                bfs_visited[i] = True

dfs(v)
print()
bfs(v)