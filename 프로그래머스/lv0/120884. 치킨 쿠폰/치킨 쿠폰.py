def solution(chicken):
    res = 0
    
    while chicken >= 10:
        res += chicken // 10
        chicken = (chicken // 10) + (chicken % 10)
    
    return res