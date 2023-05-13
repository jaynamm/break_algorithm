def solution(s):
    result = ''
    
    for c in sorted(list(set(s))):
        if s.count(c) == 1:
            result += c
    
    return result