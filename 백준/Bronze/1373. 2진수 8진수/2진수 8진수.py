import sys

binary_number = str(sys.stdin.readline().strip())
decimal_number = int(binary_number, 2)
print("{0:o}".format(decimal_number))