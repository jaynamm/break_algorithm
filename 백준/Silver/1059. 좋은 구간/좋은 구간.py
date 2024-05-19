import sys

L = int(sys.stdin.readline())
S = sorted(list(map(int, sys.stdin.readline().split())))
n = int(sys.stdin.readline())

left, right = 0, 0

if n in S:
    print(0)
else:
    for i in range(L):
        if S[i] < n:
            left = S[i]
        elif S[i] > n:
            right = S[i]
            break
            
    print((n - left) * (right - n) - 1)