import sys

RING_STR = sys.stdin.readline().strip()
N = int(sys.stdin.readline())

length = len(RING_STR)
find_count = 0


for _ in range(N):
    ring = sys.stdin.readline().strip()
    
    for i in range(len(ring)):
        if ring[i] == RING_STR[0]:
            check_str = ring[i:] + ring[:i]
            
            if check_str[:length] == RING_STR:
                find_count += 1
                break
    
    
print(find_count)