def solution(array):
    answer = 0
    
    for arr in array:
        for a in str(arr):
            if "7" in a:
                answer += 1
    
    return answer