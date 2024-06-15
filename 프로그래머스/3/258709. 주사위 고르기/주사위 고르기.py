from itertools import combinations, product
from bisect import bisect_left

def get_dice_comb_sum(dice, dice_number):
    # 각 주사위의 숫자 리스트 가져온다.
    all_dice_list = [dice[num] for num in dice_number]    
    
    # 주사위를 던질 경우 모든 조합을 구한다.
    dice_comb = list(product(*all_dice_list))
    
    # 각 조합의 합을 구해준다.
    dice_sum_list = sorted([sum(comb) for comb in dice_comb])
    
    return dice_sum_list

def solution(dice):
    answer = []
    
    # A, B 각자 주사위 절반을 가져간다. 따라서, 총 주사위의 갯수를 반으로 나눈다.
    n = len(dice)
    half = n // 2
    
    dice_number = [i for i in range(n)]
    dice_number_comb = []
    
    # Step 1 : A 와 B 가 가져가는 주사위 번호 조합을 구한다.
    A_dice_number_comb = list(combinations(dice_number, half))
    
    for A_dice_number in A_dice_number_comb:
        B_dice_number = list(set(dice_number) - set(A_dice_number))
        dice_number_comb.append([A_dice_number, B_dice_number])
    
    max_win = 0
    
    for A_dice_number, B_dice_number in dice_number_comb:
        # Step 2: A 와 B 가 가진 주사위를 던졌을 경우의 합 리스트
        A_dice_sum_comb = get_dice_comb_sum(dice, A_dice_number)
        B_dice_sum_comb = get_dice_comb_sum(dice, B_dice_number)
        
        win = 0
        
        # Step 3 : A 주사위의 합과 B 주사위의 합을 모두 비교해서 승무패를 계산한다.
        for a_sum in A_dice_sum_comb:
            win += bisect_left(B_dice_sum_comb, a_sum)

        # Step 4 : 승이 많은 주사위 조합을 가져와서 index + 1 을 해준다.
        if max_win < win:
            max_win = win
            answer = [num+1 for num in A_dice_number]

    
    return answer