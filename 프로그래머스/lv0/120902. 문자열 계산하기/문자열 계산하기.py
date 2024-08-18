def solution(my_string):
    answer = 0
    oper = ""
    
    for s in my_string.split():
        if s == "+":
            oper = "+"
        elif s == "-":
            oper = "-"
        else:
            if oper == "+":
                answer += int(s)
            elif oper == "-":
                answer -= int(s)
            else:
                answer = int(s)

    return answer