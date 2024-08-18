def solution(before, after):
    for b in before:
        if before.count(b) != after.count(b):
            return 0
    return 1