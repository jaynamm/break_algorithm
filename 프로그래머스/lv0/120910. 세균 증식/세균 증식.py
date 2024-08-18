def solution(n, t):
    answer = n
    for i in range(1, t+1):
        answer += n
        n *= 2
    
    return answer