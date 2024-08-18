n = int(input())
nums = sorted(list(map(int, input().split())))

left = 0
right = n-1

ans = abs(nums[left] + nums[right])
final = [nums[left], nums[right]]

while left < right:
    lv = nums[left]
    rv = nums[right]
    
    sum = lv + rv
    
    if abs(sum) < ans:
        ans = abs(sum)
        final = [lv, rv]
        
        if ans == 0:
            break
            
    if sum < 0:
        left += 1
    else:
        right -= 1
        
print(final[0], final[1])