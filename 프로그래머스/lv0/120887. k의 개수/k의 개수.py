def solution(i, j, k):
    answer = "".join([str(n) for n in range(i, j+1)])
    return list(answer).count(str(k))