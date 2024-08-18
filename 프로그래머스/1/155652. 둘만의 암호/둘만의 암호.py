def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    skipped = [a for a in alphabet if a not in skip]
    
    for c in s:
        answer += skipped[(skipped.index(c) + index) % len(skipped)]
    
    return answer
