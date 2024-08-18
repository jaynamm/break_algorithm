n,m = map(int, input().split())
hn = []
hm = []

for _ in range(n):
    hn.append(list(map(int, input().split())))

for _ in range(n):
    hm.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        print(int(hn[i][j]) + int(hm[i][j]), end=" ")
    print()