def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_cap = 0
    p_cap = 0
    
    for i in range(n-1, -1, -1):
        cnt  = 0
        
        d_cap -= deliveries[i]
        p_cap -= pickups[i]
        
        while d_cap < 0 or p_cap < 0:
            d_cap += cap
            p_cap += cap
            cnt += 1
            
        answer += (i+1) * cnt * 2
    
    return answer