import sys

n, m = map(int, sys.stdin.readline().split())

puzzle = []

for i in range(n):
    row = list(sys.stdin.readline().strip())
    puzzle.append(row)

start = []

for i in range(n):
    for j in range(m):
        garo = False
        
        if puzzle[i][j] == "#":
            continue
        
        # 가로 시작점 확인
        if j - 1 < 0 or puzzle[i][j-1] == "#":
            if j + 2 < m and puzzle[i][j+1] == "." and puzzle[i][j+2] == ".":
                start.append([i+1, j+1])
                garo = True
                      
        # 세로 시작점 확인
        if i - 1 < 0 or puzzle[i-1][j] == "#":
            if i + 2 < n and puzzle[i+1][j] == "." and puzzle[i+2][j] == ".":
                if not garo:
                    start.append([i+1, j+1])
                
print(len(start))
for s in start:
    print(s[0], s[1])