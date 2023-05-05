def solution(s):
    answer = [-1]
    
    for i in range(1, len(s)):
        cnt = 0
        check = False
        
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                check = True
                answer.append(i-j)
                cnt = 0
                break
            else:
                cnt += 1
        if check == False:
            answer.append(-1)
    
    return answer