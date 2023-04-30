def solution(numbers):
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range(len(alpha)):
        numbers = numbers.replace(alpha[i], number[i])
    
    return int(numbers)