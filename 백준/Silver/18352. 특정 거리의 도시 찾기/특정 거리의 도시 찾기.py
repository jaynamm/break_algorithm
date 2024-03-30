"""
도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
"""

import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)  # -1로 초기화
distance[X] = 0  # 출발 도시는 0 으로 설정

queue = deque([X])

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1  # 방문 처리
            queue.append(next_node)

check = False

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)