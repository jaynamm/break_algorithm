def dfs(depth, index):
    global _min
    
    if depth == n//2:
        start, link = 0, 0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        _min = min(_min, abs(start-link))
        return
    
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False
            
n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
_min = 1e9

dfs(0, 0)
print(_min)