def solution(s):
    answer = [-1]
    
    for i in range(1, len(s)):
        check = False
        
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                check = True
                answer.append(i-j)
                break
        if check == False:
            answer.append(-1)
    
    return answer