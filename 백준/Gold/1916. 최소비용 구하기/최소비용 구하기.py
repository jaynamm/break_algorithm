"""
N 개의 도시, 도시 번호는 1 부터 N 까지
M 개의 버스
"""

import sys

# from collections import deque
import heapq

# 도시의 개수 N, 버스의 개수 M
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
distance = [int(1e9)] * (N + 1)

for _ in range(M):
    # 출발 도시 u, 도착 도시 v, 버스 비용 w
    u, v, w = map(int, sys.stdin.readline().split())

    graph[u].append((v, w))

start, end = map(int, sys.stdin.readline().split())


def dijkstra(start):
    # q = deque([start])
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # now = q.popleft()
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # q.append(i[0])
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(distance[end])
