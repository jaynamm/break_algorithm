def solution(a, b):
    answer = 0
    rest = []
    m, n = a, b
    
    # 최대공약수 구하기
    while n:
        m, n = n, m % n
    gcd = m
    
    # 최대 공약수로 나누기
    a, b = a // gcd, b // gcd
    
    # 정수는 유한소수
    if a == b:
        answer = 1
    else:
        # 소인수 구하기
        for i in range(2, b+1):
            while b % i == 0:
                rest.append(i)
                b = b // i
    
    # 소인수에 2 와 5 만 있는지 all() 를 통해 확인
    if all(x in (2,5) for x in rest):
        answer = 1
    else:
        answer = 2
    
    return answer