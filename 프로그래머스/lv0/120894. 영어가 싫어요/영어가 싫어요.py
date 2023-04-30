def solution(numbers):
    for i, a in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(a, str(i))
    
    return int(numbers)