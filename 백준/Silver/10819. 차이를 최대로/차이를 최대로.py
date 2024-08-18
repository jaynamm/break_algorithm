n = int(input())
# n = 6
a = list(map(int, input().split()))
# a = [20, 1, 15, 8, 4, 10]

visited = [False] * n
perm = [0] * n
max_sum = 0

def backtracking(index):    
    global max_sum
    
#     print()
#     print("===== index = ", index, " =====")
    
    if index == n:
#         print("perm = ", perm)
        temp_sum = 0
        for i in range(n-1):
            temp_sum += abs(perm[i]-perm[i+1])
            
#         print("max_sum = ", max_sum, " / temp_sum = ", temp_sum)
        max_sum = max(max_sum, temp_sum)
        return

    for i in range(n):
#         print("visited[", i, "] = ", visited[i])
        if not visited[i]:
            visited[i] = True
            perm[index] = a[i]
#             print("perm[", index, "] = ", a[i])
            backtracking(index+1)
            visited[i] = False            
    
backtracking(0)

print(max_sum)