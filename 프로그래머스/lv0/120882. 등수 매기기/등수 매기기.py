def solution(score):
    rank = {}
    
    for i, aver in enumerate(sorted([(s[0]+s[1])/2 for s in score], reverse=True)):
        if aver in rank.keys():
            continue
        else:
            rank[aver] = i+1
    
    answer = [rank[s] for s in [(s[0]+s[1])/2 for s in score]]
    
    return answer