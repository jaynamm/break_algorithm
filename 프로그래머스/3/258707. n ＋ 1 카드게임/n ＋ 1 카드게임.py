def solution(coin, cards):
    game_round = 1
    n = len(cards)
    
    # 받은 카드
    my_cards = cards[:n//3]
    # 뽑은 카드
    keep_cards = []
    # 남은 카드
    cards = cards[n//3:][::-1]
    
    while True:
        # 만약 남은 카드가 없는 경우
        if len(cards) == 0:
            break
        
        # 두 장의 카드를 뽑는다.
        keep_cards.append(cards.pop())
        keep_cards.append(cards.pop())
        
        is_find = False
        
        # 필요한 카드가 모두 내 카드에만 있는 경우
        for card in my_cards:
            # 필요한 카드
            target = (n+1) - card
            
            if target in my_cards and len(cards) >= 2:
                my_cards.remove(card)
                my_cards.remove(target)
                game_round += 1
                is_find = True
                break
                
        if is_find:
            continue
            
        is_find = False
            
        # 필요한 카드가 내 카드와 뽑은 카드에 있는 경우
        for card in my_cards:
            # 필요한 카드
            target = (n+1) - card
            
            if target in keep_cards:
                if coin >= 1:
                    my_cards.remove(card)
                    keep_cards.remove(target)
                    game_round += 1
                    coin -= 1
                    is_find = True
                    break
        
        if is_find:
            continue
        
        is_find = False
            
        # 필요한 카드가 뽑은 카드에만 있는 경우
        for card in keep_cards:
            
            # 필요한 카드
            target = (n+1) - card
            
            if target in keep_cards and card != target:
                
                if coin >= 2:
                    keep_cards.remove(card)
                    keep_cards.remove(target)
                    game_round += 1
                    coin -= 2
                    is_find = True
                    break
                    
        if is_find:
            continue
                
        break
        
    return game_round