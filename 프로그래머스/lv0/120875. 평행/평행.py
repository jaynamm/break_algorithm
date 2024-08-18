def inclination(x1, y1, x2, y2):
    return abs(x2-x1) / abs(y2-y1)

def solution(dots):
    answer = 0
    
    # 기울기 = (y2-y1) / (x2-x1)
    
    # (1,2) - (3,4)
    if inclination(dots[0][0], dots[0][1], dots[1][0], dots[1][1]) == inclination(dots[2][0], dots[2][1], dots[3][0], dots[3][1]):
        answer = 1
    # (1,3) - (2,4)
    elif inclination(dots[0][0], dots[0][1], dots[2][0], dots[2][1]) == inclination(dots[1][0], dots[1][1], dots[3][0], dots[3][1]):
        answer = 1
    # (1,4) - (2,3)
    elif inclination(dots[0][0], dots[0][1], dots[3][0], dots[3][1]) == inclination(dots[1][0], dots[1][1], dots[2][0], dots[2][1]):
        answer = 1
        
    return answer