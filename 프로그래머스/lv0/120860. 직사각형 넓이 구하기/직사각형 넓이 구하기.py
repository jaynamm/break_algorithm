def solution(dots):
    x1, y1 = min(dots)
    x2, y2 = max(dots)
    return (x2-x1) * (y2-y1)