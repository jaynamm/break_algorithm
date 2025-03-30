import sys

n, m = map(int, sys.stdin.readline().split())

basket = [i + 1 for i in range(n)]

for i in range(m):
    i, j = map(int, sys.stdin.readline().split())
    basket[i - 1 : j] = reversed(basket[i - 1 : j])

print(" ".join(map(str, basket)))
