import sys

n, m = map(int, sys.stdin.readline().split())

basket = [i + 1 for i in range(n)]

for i in range(m):
    i, j = map(int, sys.stdin.readline().split())

    temp = basket[i - 1]
    basket[i - 1] = basket[j - 1]
    basket[j - 1] = temp

print(" ".join(map(str, basket)))
