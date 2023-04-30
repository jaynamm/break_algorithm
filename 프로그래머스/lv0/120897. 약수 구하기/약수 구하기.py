def solution(n):
    answer = []
    
    for i in range(1, int((n**0.5)+1)):
        if n % i == 0:
            answer += [i, n//i]
    
    answer = list(set(answer))
    answer.sort()
    
    return answer