import math

def solution(progresses, speeds):
    answer = []
    deploy = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) < 0:
            r = 0
        else:
            r = math.ceil((100 - progresses[i]) / speeds[i])
        
        print("r = ", r)
        
        if len(deploy) == 0:
            deploy.append([r, 1])
            print(deploy)
        else:
            if r <= int(deploy[-1][0]):
                deploy[-1][1] += 1
                print(deploy)
            else:
                deploy.append([r, 1])
                print(deploy)

    answer = [dep[1] for dep in deploy]
    
    return answer