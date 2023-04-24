def solution(emergency):
    answer = []
    em = {}
    
    for i, e in enumerate(sorted(emergency, reverse=True)):
        em[e] = i+1
        
    for e in emergency:
        answer.append(em[e])
        
    return answer