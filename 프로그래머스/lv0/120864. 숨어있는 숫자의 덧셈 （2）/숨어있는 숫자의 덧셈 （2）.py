import re

def solution(my_string):
    return sum(list(map(int, re.sub("[a-z]|[A-Z]", " ", my_string).split())))