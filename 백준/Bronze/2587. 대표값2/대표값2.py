num = [int(input()) for _ in range(5)]
num.sort()

print(sum(num)//len(num))
print(num[len(num)//2])