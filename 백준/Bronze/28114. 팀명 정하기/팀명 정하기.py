p = [list(map(str, input().split())) for _ in range(3)]
    
p.sort(key = lambda x : int(x[1])%100)
print(p[0][1][-2:]+p[1][1][-2:]+p[2][1][-2:])

p.sort(key = lambda x : int(x[0]), reverse=True)
print(p[0][2][:1]+p[1][2][:1]+p[2][2][:1])