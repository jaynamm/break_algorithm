def solution(board):
    answer = 0
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    boom = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                boom.append([i, j])
    
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board):
                board[nx][ny] = 1
                
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                answer += 1
            
    return answer