def solution(balls, share):
    answer = 0
    a = 1
    b = 1
    for i in range(share):
        a *= balls-i
        b *= share-i
    answer = a//b
    return answer