import sys

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]
    
def union(root, x, y):
    root_x = find(root[x])
    root_y = find(root[y])
    
    if root_x != root_y:
        root[root_y] = root_x

n, m = map(int, sys.stdin.readline().split())

root = list(range(n + 1))

for _ in range(m):
    oper, a, b = map(int, sys.stdin.readline().split())
    
    # union 연산
    if oper == 0:
        union(root, a, b)
    # find 연산
    elif oper == 1:
        root_a = find(a)
        root_b = find(b)
    
        if root_a == root_b:
            print("YES")
        else:
            print("NO")