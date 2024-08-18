def solution(park, routes):
    start = []
    
    for i in range(len(park)):
        if "S" in park[i]:
            start = [i, park[i].find("S")]
            break
                
    print("start = ", start)
    
    for route in routes:
        op, n = route.split()
        n = int(n)
        
        if op == "N":
            if start[0] - n < 0:
                continue
            if 'X' in [park[i][start[1]] for i in range(start[0]-n, start[0])]:
                continue
            else:
                start[0] -= n
        elif op == "S":
            if start[0] + n >= len(park):
                continue
            if 'X' in [park[i][start[1]] for i in range(start[0]+1, start[0]+n+1)]:
                continue
            else:
                start[0] += n
        elif op == 'W':
            if start[1] - n < 0:
                continue    
            if 'X' in park[start[0]][start[1]-n:start[1]]:
                continue
            else:
                start[1] -= n
        elif op == 'E':
            if start[1] + n >= len(park[0]):
                continue
            if 'X' in park[start[0]][start[1]+1:start[1]+n+1]:
                continue
            else:
                start[1] += n

    return start