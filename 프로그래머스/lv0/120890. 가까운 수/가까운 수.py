def solution(array, n):
    mi = 100 
    answer = 0
    
    for a in array:
        if abs(n-a) < mi:
            mi = min(abs(n-a), mi)
            answer = a
        elif abs(n-a) == mi:
            answer = min(answer, a)
        
    return answer