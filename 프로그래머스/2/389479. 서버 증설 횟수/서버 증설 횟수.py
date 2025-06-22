def solution(players, m, k):
    answer = 0
    
    server = [[(p // m), 0, 0] for p in players]
    
    for i in range(len(server)):
        # 필요한 서버의 수: server[i][0]
        # 현재 서버수 : server[i][1]
        # 증설한 서버 횟수: server[i][2]
        
        if server[i][0] > server[i][1]:
            # 증설이 필요한 서버 수 = 필요한 서버 수 - 현재 서버 수
            need = server[i][0] - server[i][1]
            
            # 서버 증설 횟수 증가시킨다.
            server[i][2] += need
            
            # 서버를 증설할 경우 최대 24시간을 넘기지 않도록 한다.
            end = min(i + k, len(server))
            
            # k 시간만큼 서버를 증설해준다.
            for j in range(i, end):
                server[j][1] += need
    
    # 서버를 증설한 횟수를 모두 더해준다.
    answer = sum([s[2] for s in server])
    
    return answer