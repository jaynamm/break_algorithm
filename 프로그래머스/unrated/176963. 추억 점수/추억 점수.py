def solution(name, yearning, photo):
    answer = []
    ny = {name[i]:yearning[i] for i in range(len(name))}
    
    for p in photo:
        sum = 0
        
        for i in range(len(p)):
            if p[i] in ny:
                sum += ny[p[i]]

        answer.append(sum)
    
    return answer