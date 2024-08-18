import sys

n = int(sys.stdin.readline())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

nums.sort(key = lambda x:(x[1], x[0]))

for i in range(n):
    print(*nums[i])