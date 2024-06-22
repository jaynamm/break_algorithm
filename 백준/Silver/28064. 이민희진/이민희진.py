import sys

# n 명의 사람
n = int(sys.stdin.readline())

name_list = []

for i in range(n):
    name = sys.stdin.readline().strip()
    name_list.append(name)

match = 0
    
for i in range(n):
    for j in range(i+1, n):
        min_length = min(len(name_list[i]), len(name_list[j]))
        cur = 1
        
        while min_length >= cur:
            if name_list[i][-cur:] == name_list[j][:cur]:
                match += 1
                break
            elif name_list[j][-cur:] == name_list[i][:cur]:
                match += 1
                break
            
            cur += 1
            
print(match)
    