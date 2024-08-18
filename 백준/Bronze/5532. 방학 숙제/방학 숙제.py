import sys
import math

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

print(L - max(math.ceil(A / C), math.ceil(B / D)))