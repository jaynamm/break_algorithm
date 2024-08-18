"""
지름길 개수 N (N <= 12), 즉 지름길의 개수는 12개 이하
고속도로의 길이 D (D <= 10,000)

지름길의 시작위치, 도착위치, 지름길의 길이가 주어진다.
모든 위치와 길이는 10,000 이하의 자연수이다.
"""

import sys
from collections import deque

INF = int(1e9)

N, D = map(int, sys.stdin.readline().split())

# 거리는 초기값으로 무한대로 설정해준다.
# distance 에는 각 지점까지의 최단 거리를 저장한다.
distance = [INF] * (D + 1)
# 최대 거리 만큼 graph를 만들어준다.
graph = [[] for _ in range(D + 1)]

# i = 0 일 때, graph[0] = [(1, 1)] 인 이유는 0에서 1로 가는 거리가 1이기 때문
# i = 1 일 때, graph[1] = [(2, 1)] 인 이유는 1에서 2로 가는 거리가 1이기 때문
# 이후 값들을 동일하게 설정해준다.
for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())

    # 도착지점이 D보다 크다면, 지름길을 사용할 수 없다.
    if end > D:
        continue

    # 지름길의 시작점과 끝점, 거리를 추가해준다.
    # 만약 위에서 start, end, length = 0 50 10 이 추가된다면, graph[0] = [(1, 1), (50, 10)] 이 된다.
    graph[start].append((end, length))

# 시작은 거리가 0부터 시작하기 때문에 0을 넣어준다.
queue = deque([(0, 0)])
# 거리는 시작점이 0이기 때문에 0으로 설정해준다.
distance[0] = 0

# queue 가 빌 때까지 반복한다.
while queue:
    node, dist = queue.popleft()

    # 만약 현재 거리보다 더 멀다면, 무시한다.
    if dist > distance[node]:
        continue

    # graph[node] 는 현재 노드에서 갈 수 있는 다음 노드들을 의미한다.
    # 예를 들어, graph[node] = (0, 0) 이라면, [(1, 1), (50, 10)] 이 된다.
    for next_node, next_dist in graph[node]:
        # 다음 도착 노드의 거리는 현재 거리부터 다음 거리를 더한 값이다.
        cost = dist + next_dist

        # 만약 다음 도착 노드의 거리가 현재 거리보다 작다면, 갱신해준다.
        if cost < distance[next_node]:
            distance[next_node] = cost
            queue.append((next_node, cost))

# 마지막으로 도착지점의 거리를 출력한다.
# distance[D] 는 D까지의 최단 거리를 의미한다.
print(distance[D])
