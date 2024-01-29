def solution(friends, gifts):
    answer = 0
    length = len(friends)
    
    # Create Table - 선물을 준 횟수
    give = [[0] * length for _ in range(length)]
    
    for gift in gifts:
        giver, taker = gift.split()

        give_id = friends.index(giver)
        take_id = friends.index(taker)

        give[give_id][take_id] += 1
        
    print(give)
    
    # Calculate
    score = [0] * len(friends)

    for i in range(length):
        for j in range(i+1, length):
            give_score = give[i][j] # i 가 j 에게 준 선물 개수
            take_score = give[j][i] # j 가 i 에게 준 선물 개수
            
            if (give_score != take_score) and (give_score > 0 or take_score > 0):
                if give_score > take_score:
                    score[i] += 1
                else:
                    score[j] += 1
            else:
                give_sum = sum(give[i])
                take_sum = sum(give[j])
                
                for k in range(length):
                    give_sum -= give[k][i]
                    take_sum -= give[k][j]
                
                if give_sum > take_sum:
                    score[i] += 1
                elif give_sum < take_sum:
                    score[j] += 1
                    
    print(score)
    
    answer = max(score)
    
    return answer