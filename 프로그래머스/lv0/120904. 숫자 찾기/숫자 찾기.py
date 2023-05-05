def solution(num, k):
    answer = []
    numlist = []
    
    while num > 0:
        numlist.append(num % 10)
        num = num // 10
    
    answer = numlist[::-1]
    
    if k in answer:
        return answer.index(k) + 1
    else:
        return -1