# 1) 선물을 더 많이 준 사람이 선물 +1 받음
# 2) 선물 받은 기록 없음 or 같음 -> 선물지수가 더 큰 사람에게 +1 받음, 만약 선물지수가 같다면 없음

def solution(friends, gifts):
    answer = 0
    
    # 친구 수
    length = len(friends)

    # 선물을 주고받은 데이터를 저장할 2중 배열 생성
    give = [[0] * length for _ in range(length)]
    
    for gift in gifts:
        # 선물을 준 사람과 받은 사람을 가져온다.
        giver, taker = gift.split()
        
        # 준 사람과 받은 사람의 인덱스를 가져온다.
        give_id = friends.index(giver)
        take_id = friends.index(taker)
        
        # 배열에 추가한다.
        give[give_id][take_id] += 1
    
    result = [0] * length
    
    for i in range(length):
        for j in range(i+1, length):
            # i 가 j 에게 준 선물 개수
            give_score = give[i][j] 
            # j 가 i 에게 준 선물 개수 = i 가 j 에게 받은 선물 개수
            take_score = give[j][i] 
            
            # 조건 1: 주고받은 선물의 개수가 같지 않고 한 명의 친구가 선물을 준 경우
            if (give_score != take_score) and (give_score > 0 or  take_score > 0):
                # 조건 1-1: 선물을 더 많이 준 친구가 선물 하나를 받는다.
                if give_score > take_score:
                    result[i] += 1
                else:
                    result[j] += 1
            # 조건 2: 주고받은 선물이 없는 경우
            else:
                # 조건 2-1: 선물지수가 높은 친구가 선물 하나를 받는다.
                # 준 선물의 수 = 행(row)의 합
                # 받은 선물의 수 = 열(column)의 합
                
                # i 가 준 선물 개수
                give_sum = sum(give[i])
                # j 가 준 선물 개수
                take_sum = sum(give[j])
                
                # 선물 지수를 구한다.
                # 선물 지수 = 준 선물 - 받은 선물
                for k in range(length):
                    give_sum -= give[k][i]
                    take_sum -= give[k][j]
                    
                # 선물지수 비교
                if give_sum > take_sum:
                    result[i] += 1
                elif give_sum < take_sum:
                    result[j] += 1
                    
    # 선물을 가장 많이 받는 친구의 선물 개수를 구한다.
    answer = max(result)
                
    return answer