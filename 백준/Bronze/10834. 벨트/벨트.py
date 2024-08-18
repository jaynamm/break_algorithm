import sys

# m : 벨트의 개수
m = int(sys.stdin.readline())

# m + 1 의 방향과 회전 수를 저장
belt_direction = 0
belt_rotation = 1

# a : 벨트의 앞 바퀴, b : 벨트의 뒷 바퀴, s : 벨트의 형태 (0: 0자, 1: 8자)
for _ in range(m):
    a, b, s = map(int, sys.stdin.readline().split())
    
    if s == 1: # 반시계 방향
        belt_direction = 1 if belt_direction == 0 else 0
        
    belt_rotation = belt_rotation // a * b 
        
print(belt_direction, belt_rotation)