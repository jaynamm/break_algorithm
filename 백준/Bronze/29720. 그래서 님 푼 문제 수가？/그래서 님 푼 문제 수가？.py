import sys

# 총 n 문제 이상 해결 -> 하루 M 문제씩 -> 회소 K 일은 풀어야 한다.
n, m, k = map(int, sys.stdin.readline().split())

min_solved = max(0, n - (m * k))
max_solved = max(0, n - m * (k - 1) - 1)

print(min_solved, max_solved)
