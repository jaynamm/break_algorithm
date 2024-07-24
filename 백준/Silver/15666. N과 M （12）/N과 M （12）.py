import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()

answer = []

for i in combinations_with_replacement(num_list, m):
    answer.append(list(i))

for num in sorted(list(set(map(tuple, answer)))):
    print(' '.join(map(str, num)))
        