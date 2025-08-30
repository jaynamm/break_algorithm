from collections import deque

def solution(land):
    answer = 0
    
    # land 의 가로와 세로 길이
    height, width = len(land), len(land[0])
    # 방문 리스트는 land 와 동일한 크기를 가진다.
    visited = [[False] * width for _ in range(height)]
    # 상하좌우를 살피기 위한 좌표 리스트
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 문제에서 가장 많은 석유량을 가지고 있는 시추관을 계산하기 위한 리스트
    # 즉, 각 열 중에서 가장 석유량이 많은 열을 가져와야 한다.
    oil = [0] * width  
    
    for h in range(height):
        for w in range(width):
            # 방문하지 않았는데 석유가 있는 경우
            if land[h][w] == 1 and not visited[h][w]:
                queue = deque()  # 큐를 생성한다.
                queue.append([h, w])  # 큐에 방문한 위치를 넣는다.
                
                count = 1  # 기름 갯수
                
                oil_cols = {w}  # 석유가 있는 열을 확인하기 위한 SET
                
                # 석유가 없을 때까지 계속 탐색한다.
                while queue:
                    qx, qy = queue.popleft()  # 큐에서 위치를 가져온다.
                    visited[qx][qy] = True  # 방문했다고 표시한다.
                    
                    # 현재 위치에서 상하좌우를 살핀다.
                    for x, y in directions:
                        dx, dy = qx + x, qy + y
                        
                        # 상하좌우가 land 안에 있는지 확인한다.
                        if 0 <= dx < height and 0 <= dy < width:
                            # 만약 석유가 있는데 방문하지 않았을 경우
                            if land[dx][dy] == 1 and not visited[dx][dy]:
                                queue.append([dx, dy])  # 석유가 있는 위치를 큐에 넣어준다.
                                visited[dx][dy] = True  # 방문했다고 표시한다.
                                count += 1  # 석유 1개를 추가한다.
                                
                                oil_cols.add(dy)  # 석유가 있는 열을 추가한다.
                                
                # 석유가 있는 위치를 모두 확인했다면 각 열에 석유량을 더해준다.
                for col in oil_cols:
                    oil[col] += count
    
    # 각 열 중 석유가 가장 많은 열을 찾는다.
    answer = max(oil)
    
    return answer