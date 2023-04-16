def solution(keyinput, board):
    answer = [0, 0]
    
    for key in keyinput:
        xsize = board[0] // 2
        ysize = board[1] // 2
        
        if key == "up":
            if answer[1] + 1 > ysize:
                continue
            else:
                answer[1] += 1
        elif key == "down":
            if answer[1] - 1 < -ysize:
                continue
            else:
                answer[1] -= 1
        elif key == "left":
            if answer[0] - 1 < -xsize:
                continue
            else:
                answer[0] -= 1
        elif key == "right":
            if answer[0] + 1 > xsize:
                continue
            else:
                answer[0] += 1
    
    return answer