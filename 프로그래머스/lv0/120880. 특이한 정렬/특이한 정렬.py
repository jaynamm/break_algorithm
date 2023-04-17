def solution(numlist, n):
    answer = []
    gap = []
    
    for num in numlist:
        gap.append([num, abs(n-num)])
    
    gap.sort(key = lambda x:(x[1], x[0]))
    
    answer.append(gap[0][0])
    
    for i in range(1, len(gap)):
        if gap[i-1][1] == gap[i][1]:
            answer[i-1] = gap[i][0]
            answer.append(gap[i-1][0])
        else:
            answer.append(gap[i][0])
    
    return answer