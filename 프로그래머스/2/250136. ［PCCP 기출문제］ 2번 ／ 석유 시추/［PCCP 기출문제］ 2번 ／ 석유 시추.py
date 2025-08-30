from collections import deque

def solution(land):
    answer = 0
    
    # 총 길이 : 세로 h, 가로 w
    h, w = len(land), len(land[0])

    # 방문 여부 크기는 land 와 동일하고 값은 False 로 초기화
    visited = [[False] * w for _ in range(h)]
    
    # 탐색 시 상하좌우 계산을 하기 위한 리스트
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    oil_sum = [0] * w
    
    for i in range(h):
        for j in range(w):
            # 기름이 있는데 방문하지 않은 경우
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append([i, j])

                oil_count = 1
                oil_cols = {j}
                
                # 큐에 남아있는 경우
                while queue:                    
                    qh, qw = queue.popleft()
                    visited[qh][qw] = True
                    
                    for x, y in directions:
                        dx, dy = qh + x, qw + y
                        
                        # land 범위에 들어오는 경우
                        if 0 <= dx < h and 0 <= dy < w:
                            # 기름이 있는데 방문하지 않는 경우
                            if land[dx][dy] == 1 and not visited[dx][dy]:
                                queue.append([dx, dy])
                                visited[dx][dy] = True
                                oil_count += 1
                                
                                oil_cols.add(dy)
                                
                for col in oil_cols:
                    oil_sum[col] += oil_count
                
    answer = max(oil_sum)
    
    return answer