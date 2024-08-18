import sys

n, s = map(str, sys.stdin.readline().strip().split())
n = int(n)

winner_index = 0
winner_answer = ""

chats = []

for i in range(n):
    nickname, answer = map(str, sys.stdin.readline().split())
    
    if nickname == s:
        winner_index = i
        winner_answer = answer
        
    chats.append([nickname, answer])

cnt = 0

for i in range(winner_index):
    if chats[i][1] == winner_answer:
        cnt += 1
        
print(cnt)