def solution(quiz):
    answer = []
    
    for q in quiz:
        spt = list(map(str, q.split()))
        result = 0
        if spt[1] == '+':
            result = int(spt[0]) + int(spt[2])
            if result == int(spt[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif spt[1] == '-':
            result = int(spt[0]) - int(spt[2])
            if result == int(spt[4]):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer