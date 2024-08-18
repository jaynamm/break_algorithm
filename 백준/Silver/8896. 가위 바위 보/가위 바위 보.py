import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    robots = []

    for _ in range(N):
        robot = sys.stdin.readline().strip()
        robots.append(robot)

    result = [True] * N
    k = len(robots[0])
    
    for i in range(k):
        rsp = [0] * 3
        
        for j in range(N):
            if not result[j]:
                continue
            if robots[j][i] == "R":
                rsp[0] = 1
            elif robots[j][i] == "S":
                rsp[1] = 1
            elif robots[j][i] == "P":
                rsp[2] = 1
        
        loser = ""
        
        if sum(rsp) == 2:
            # 주먹이 없는 경우, 가위 vs 보
            if rsp[0] == 0:
                loser = "P"
            # 가위가 없는 경우, 주먹 vs 보
            elif rsp[1] == 0:
                loser = "R"
            # 보가 없는 경우, 주먹  vs 가위
            elif rsp[2] == 0:
                loser = "S"
                
        for j in range(N):
            if robots[j][i] == loser:
                result[j] = False
                
    if result.count(True) == 1:
        print(result.index(True) + 1)
    else:
        print(0)