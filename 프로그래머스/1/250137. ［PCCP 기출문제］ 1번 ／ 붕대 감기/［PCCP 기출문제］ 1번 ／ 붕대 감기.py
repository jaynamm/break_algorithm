def solution(bandage, health, attacks):
    # bandage = t: 시전 시간 / x: 1초당 회복량 / y: 연속으로 성공 시 추가 회복량
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    
    # 현재 시간, 0초에서 시작
    current_time = 0
    # 최대 체력
    max_health = health
    
    for attack in attacks:
        # 공격 시간, 피해량
        attack_time = attack[0]
        attack_damage = attack[1]
        
        # 힐링 시간 = 공격 받은 시간 - 현재 시간 - 1 (공격 받는 시간 제외)
        healing_time = attack_time - current_time - 1
        
        # 만약 연속 성공 시간이 된다면 추가 회복 한다.
        healing_amount = (x * healing_time) + (y * (healing_time // t))
        
        # 힐을 받은 체력이 최대 체력보다 많은 경우
        if (health + healing_amount) > max_health:
            health = max_health
        else:
            health += healing_amount
        
        # 받은 공격만큼 체력을 감소한다.
        health -= attack_damage
        
        # 체력이 0이하가 되어 죽는다면 -1
        if health <= 0:
            health = -1 
            break
        
        current_time = attack_time

    return health