def solution(arr, k):
    answer = []
        
    for i in range(len(arr)):
        if len(answer) >= k:
            break
        if arr[i] not in answer:
            answer.append(arr[i])
    
    while len(answer) < k:
        answer.append(-1)
        
    return answer