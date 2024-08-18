from itertools import permutations

def solution(spell, dic):
    answer = 2
    
    for s in list(permutations(spell, len(spell))):
        if "".join(s) in dic:
            answer = 1
            break
    
    return answer