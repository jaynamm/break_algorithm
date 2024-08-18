import sys

n = int(sys.stdin.readline())

ropes = []

for _ in range(n):
    rope = int(sys.stdin.readline())
    ropes.append(rope)
    
ropes = sorted(ropes)
max_weight = 0
    
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (n-i))
    
print(max_weight)