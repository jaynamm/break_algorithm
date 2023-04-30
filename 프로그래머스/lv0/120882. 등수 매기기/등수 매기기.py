def solution(score):
    rank = {}
    
    for i, aver in enumerate(sorted([sum(s) for s in score], reverse=True)):
        if aver in rank.keys():
            continue
        else:
            rank[aver] = i+1
    
    answer = [rank[s] for s in [sum(s) for s in score]]
    
    return answer