def solution(num, k):
    return str(num).find(str(k)) + 1 if str(k) in str(num) else -1