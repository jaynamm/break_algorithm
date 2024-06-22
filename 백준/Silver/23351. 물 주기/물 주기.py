import sys

n, k, a, b = map(int, sys.stdin.readline().split())
day = 1

catnip_list = [k] * n
water_target = 0

while True:
    for water in range(water_target, water_target+a):
        catnip_list[water] += b
        
    if water_target + a == n:
        water_target = 0
    else:
        water_target += a
    
    for i in range(n):
        catnip_list[i] -= 1

    if catnip_list.count(0) > 0:
        break
    
    day += 1
    
print(day)