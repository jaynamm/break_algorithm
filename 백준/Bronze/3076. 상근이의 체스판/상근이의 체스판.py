import sys

r, c = map(int, sys.stdin.readline().split())
a, b = map(int, sys.stdin.readline().split())
 
row_color = "X"
col_color = "X"

for i in range(r * a):
    if i % a == 0:
        row_color = "X" if row_color == "." else "."
    for j in range(c * b):
        if j == 0:
            col_color = row_color
        if j % b == 0:
            col_color = "X" if col_color == "." else "."
        print(col_color, end="")
    print()