import sys

n, m = map(int, sys.stdin.readline().split())

basket = [0] * n

for i in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

    for l in range(i, j + 1):
        basket[l - 1] = k

print(" ".join(map(str, basket)))
