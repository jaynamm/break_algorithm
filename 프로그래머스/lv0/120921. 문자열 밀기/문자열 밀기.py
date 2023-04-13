def solution(A, B):
    answer = 0
    
    if A == B:
        return answer
    
    for i in range(len(A)):
        s = (A[-(1+i):] + A[:-(1+i)])
        if s == B:
            answer += 1
            break
        answer += 1
    if answer == len(A):
        answer = -1
    return answer