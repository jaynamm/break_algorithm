def merge(arr, l, mid, r):
    i, j, k = l, mid+1, l
    
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            sorted_arr[k] = arr[i]
            cnt_arr.append(arr[i])
            i += 1

        else:
            sorted_arr[k] = arr[j]
            cnt_arr.append(arr[j])
            j += 1

        k += 1
            
    if i <= mid:
        for t in range(i, mid+1):
            sorted_arr[k] = arr[t]
            k += 1
            cnt_arr.append(arr[t])
    else:
        for t in range(j, r+1):
            sorted_arr[k] = arr[t]
            k += 1            
            cnt_arr.append(arr[t])
        
    for i in range(l, r+1):
        arr[i] = sorted_arr[i]

        
def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
    
        merge_sort(arr, l, mid) # 왼쪽 배열 정렬
        merge_sort(arr, mid+1, r) # 오른쪽 배열 정렬
        merge(arr, l, mid, r) # 왼쪽 배열과 오른쪽 배열 병합

    
a, k = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = [0] * len(arr)
cnt_arr = []
merge_sort(arr, 0, len(arr)-1)

if len(cnt_arr) > k:
    print(cnt_arr[k-1])
else:
    print("-1")