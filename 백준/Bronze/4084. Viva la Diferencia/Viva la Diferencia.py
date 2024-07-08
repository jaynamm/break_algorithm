import sys

while True:
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    if a == b == c == d == 0:
        break
    
    count = 0
    
    while True:
        if a == b == c == d:
            break
        
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        count += 1
        
    print(count)