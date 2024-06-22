import sys

n, m, k = map(int, sys.stdin.readline().split())

result = [n+1, m+1]
hands_list = []

for i in range(n):
    hands = list(map(int, sys.stdin.readline().split()))    
    hands_list.append(hands)

for i, hands in enumerate(hands_list):
    people = i + 1
    hands_sum = 0
    
    for h in hands:
        hands_sum += h

    if hands_sum < k:
        continue
    
    sum = 0
    hands_count = 0
    
    for j in range(m):
        sum += hands[j]
        
        if sum >= k:
            hands_count = j + 1
            break
    
    if people < result[0] or hands_count < result[1]:
        result[0] = people
        result[1] = hands_count
        
print(result[0], result[1])