s=[0]*31

for _ in range(28):
    s[int(input())] = 1
    
for i in range(1, len(s)):
    if s[i] == 0:
        print(i)