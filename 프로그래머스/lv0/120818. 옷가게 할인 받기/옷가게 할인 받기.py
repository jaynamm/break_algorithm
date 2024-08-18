def solution(price):
    answer = price
    
    if price >= 500000:
        answer = int(price*0.8)
    elif price >= 300000:
        answer = int(price*0.9)
    elif price >= 100000:
        answer = int(price*0.95)

    return answer
    