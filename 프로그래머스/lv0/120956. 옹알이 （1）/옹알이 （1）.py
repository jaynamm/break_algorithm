from itertools import permutations

def solution(babbling):
    answer = 0
    perm = []
    perm_join = []
    
    for i in range(1, 5):
        perm.append(list(permutations(["aya", "ye", "woo", "ma"], i)))
    
    for i in range(len(perm)):
        for j in range(len(perm[i])):
            perm_join.append("".join(perm[i][j]))
            
    for bab in babbling:
        if bab in perm_join:
            answer += 1

    return answer