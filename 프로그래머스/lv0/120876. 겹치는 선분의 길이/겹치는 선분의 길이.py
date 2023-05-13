def solution(lines):
    answer = 0
    res = [0] * 201
    
    for line in lines:
        for i in range(line[0], line[1]): 
            res[i + 100] += 1
    answer += res.count(2) # 두 개 이상 겹친 점
    answer += res.count(3) # 세 개 이상 겹친 점
    return answer