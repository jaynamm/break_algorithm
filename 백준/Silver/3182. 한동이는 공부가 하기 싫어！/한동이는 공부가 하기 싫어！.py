import sys

def dfs(graph, start, visited):
    visited[start] = True
    
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

n = int(sys.stdin.readline())

graph = {}

for i in range(1, n+1):
    graph[i] = [int(sys.stdin.readline())]

result = []

for i in range(1, n + 1):
    cnt = 0
    visited = [False] * (n + 1)

    dfs(graph, i, visited)
    
    result.append(visited.count(True))
    
print(result.index(max(result)) + 1)