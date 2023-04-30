def solution(my_string, num1, num2):
    my_string = list(my_string)
    answer = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = answer
    return "".join(my_string)