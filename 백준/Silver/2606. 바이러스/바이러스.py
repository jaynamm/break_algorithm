import sys

computers = int(sys.stdin.readline())
connections = int(sys.stdin.readline())

graph = [[] for _ in range(computers + 1)]

for _ in range(connections):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computers + 1)

def dfs(v):
    visited[v] = True
    
    if len(graph[v]) == 0:
        return
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
                        
dfs(1)

print(visited.count(True)-1)