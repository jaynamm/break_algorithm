def solution(polynomial):
    answer = ''
    
    pol = list(map(str, polynomial.split(" + ")))
    
    x = []
    d = []
    
    for p in pol:
        if "x" in p:
            if len(p) == 1:
                x.append("1"+p)
            else:
                x.append(p)
        else:
            d.append(p)
            
    print(x, d)
    
    xsum = 0
    dsum = 0
    
    for i in x:
        xsum += int(i[:-1])
            
    for i in d:
        dsum += int(i)

    print(xsum, dsum)
    
    if xsum != 0 and xsum == 1:
        if dsum != 0:
            answer += "x" + " + " + str(dsum)
        else:
            answer += "x"
    elif xsum != 0 and xsum != 1:
        if dsum != 0:
            answer += str(xsum) + "x" + " + " + str(dsum)    
        else:
            answer += str(xsum) + "x"
    elif xsum == 0 and dsum != 0:
        answer += str(dsum)
    elif xsum == 0 and dsum == 0:
        answer  = "0"
    
    return answer