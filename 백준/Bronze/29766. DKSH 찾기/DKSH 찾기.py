import sys

input_text = sys.stdin.readline()

dksh = "DKSH"

count = 0

for i in range(len(input_text)):
    if input_text[i : i + 4] == dksh:
        count += 1

print(count)
