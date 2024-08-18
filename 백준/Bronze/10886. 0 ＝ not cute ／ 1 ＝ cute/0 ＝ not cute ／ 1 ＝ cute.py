import sys
n = int(sys.stdin.readline())

vote = [0, 0]

for i in range(n):
    answer = sys.stdin.readline().strip()
    
    if answer == '0':
        vote[0] += 1
    elif answer == '1':
        vote[1] += 1

if vote[0] > vote[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")