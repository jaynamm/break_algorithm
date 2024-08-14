"""
뒷 큰수 == 배열의 원소에서 자신보다 위에 이는 숫자 중 자신보다 크면서 가장 가까이 있는 수
즉, 가장 처음으로 나오는 자신보다 큰 수
"""

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)
        
    return answer