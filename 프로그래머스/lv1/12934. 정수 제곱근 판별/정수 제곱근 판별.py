def solution(n):
    answer = 0
    if round(n**(0.5))**2 == n:
        answer = (n**(0.5)+1)**2
    else:
        answer = -1
    return answer