def solution(n):
    x3 = []
    
    for i in range(1, n*2+1):
        if i % 3 == 0 or "3" in str(i):
            continue
        else:
            x3.append(i)
    
    return x3[n-1]