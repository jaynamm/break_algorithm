def solution(lines):
#     answer = 0
#     res = [0] * 201
    
#     for line in lines:
#         for i in range(line[0], line[1]): 
#             res[i + 100] += 1
#     answer += res.count(2)
#     answer += res.count(3)
#     return answer

    l = [set(range(line[0], line[1])) for line in lines]
    return len(l[0]&l[1] | l[0]&l[2] | l[1]&l[2])