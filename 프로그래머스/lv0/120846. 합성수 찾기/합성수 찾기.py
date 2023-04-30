def solution(n):
    answer = 0
    
    for i in range(4, n+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
            if cnt > 2:
                answer += 1
                break
    
    return answer