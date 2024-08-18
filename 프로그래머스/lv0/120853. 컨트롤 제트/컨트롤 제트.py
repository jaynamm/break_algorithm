def solution(s):
    answer = 0
    cal = list(map(str, s.split()))
    for i in range(len(cal)):
        answer = answer-int(cal[i-1]) if cal[i] == "Z" else answer+int(cal[i])
    
    return answer