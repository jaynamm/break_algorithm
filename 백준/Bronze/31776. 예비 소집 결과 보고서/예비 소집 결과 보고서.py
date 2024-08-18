import sys

n = int(sys.stdin.readline())

cnt = 0

for i in range(n):
    t1, t2, t3 = map(int, sys.stdin.readline().split())
    
    if t3 >= 0:
        if 0 <= t1 <= t2 and 0 <= t2 <= t3:
            cnt += 1
        else:
            continue
    elif t2 >= 0:
        if 0 <= t1 <= t2:
            cnt += 1
    elif t1 >= 0:
        cnt += 1
    else:
        continue
            
print(cnt)