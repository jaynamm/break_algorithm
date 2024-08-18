def solution(num, total):
    answer = []
    
    mid = total // num
    
    if num % 2 == 0:
        for i in range(-(num//2)+1, num//2+1):
            answer.append(mid+i)    
    else:
        for i in range(-(num//2), num//2+1):
            answer.append(mid+i)
    
    return answer