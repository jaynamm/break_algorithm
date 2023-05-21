name = str(input())
n = int(input())
ans = []

for i in range(n):
    team = str(input())
    
    L, O, V, E = (name+team).count('L'), (name+team).count('O'), (name+team).count('V'), (name+team).count('E')
    rate = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    ans.append([team, rate])
    
    
ans.sort(key=lambda x: (-x[1], x[0]))

print(ans[0][0])