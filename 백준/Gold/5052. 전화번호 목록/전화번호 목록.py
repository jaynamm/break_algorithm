import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    nums = sorted([str(sys.stdin.readline().strip()) for _ in range(n)])
    check = True
    
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")