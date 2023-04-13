def solution(array, height):
    cnt = 0
    for arr in array:
        if arr > height:
            cnt += 1
    return cnt