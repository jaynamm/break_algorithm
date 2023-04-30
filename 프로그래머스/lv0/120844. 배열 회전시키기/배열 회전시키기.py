def solution(numbers, direction):
    answer = []
    
    if direction == "left":
        answer += numbers[1:]
        answer.append(numbers[0])
    elif direction == "right":
        answer.append(numbers[-1])
        answer += numbers[:-1]
    
    return answer