# fees : default_time, default fee, part time, part fee
# records : time(HH:MM), car number, status(IN or OUT)

import math

def solution(fees, records):
    answer = {record.split()[1]:0 for record in records}
    stack = {}
    
    def_time, def_fee, part_time, part_fee = fees
    
    for record in records:
        time, cnum, status = record.split()
        
        time = int(time.split(":")[0]) * 60 + int(time.split(":")[1])
        
        if status == "IN":
            stack[cnum] = time
        elif status == "OUT":
            if cnum in stack.keys():
                total_time = time - stack.pop(cnum)
                answer[cnum] += total_time
    
    if stack:
        for car_num in stack.keys():
            answer[car_num] += 1439 - stack[car_num]
    
    result = []
    
    for key in sorted(answer.keys()):
        if answer[key] <= def_time:
            result.append(def_fee)
        else:
            total_fee = math.ceil((answer[key] - def_time) / part_time) * part_fee + def_fee
            result.append(total_fee)
    
    return result