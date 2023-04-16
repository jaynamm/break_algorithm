def solution(n):
    answer = 0
    
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            if i == n // i:
                answer += 1
            else:
                answer += 2
    
    return answer