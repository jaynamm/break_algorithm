import sys

volume = [[False] * 101 for _ in range(101)]

total = 0

for _ in range(4):
    x1, x2, y1, y2 = map(int, sys.stdin.readline().split())
    
    for i in range(x1, y1):
        for j in range(x2, y2):
            if volume[i][j]:
                continue
            
            volume[i][j] = True
            total += 1
            
print(total)