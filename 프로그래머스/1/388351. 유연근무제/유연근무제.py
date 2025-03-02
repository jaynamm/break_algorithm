def solution(schedules, timelogs, startday):
    answer = 0
    
    # 일한 직원의 수
    workers = len(schedules)
    
    # 체크할 요일 확인
    weeks = [True] * 7
    
    # 토요일 일요일 제외
    for day in range(0, 7):
        now_day = startday + day
        
        if now_day > 7:
            now_day -= 7
            
        if now_day % 6 == 0 or now_day % 7 == 0:
            weeks[day] = False
            
    for i in range(workers):
        cutline = schedules[i] + 10
        
        if cutline % 100 == 60:
            cutline = ((cutline // 100) + 1) * 100
        elif cutline % 100 > 60:
            hour = (cutline // 100) + 1
            minute = (cutline % 100) % 60
            cutline = (hour * 100) + minute
            
        success = True
        
        if schedules[i] > 1100:
            success = False
            break
        
        for j in range(len(timelogs[i])):    
            if weeks[j] == False:
                continue
            else:
                if timelogs[i][j] > cutline:
                    success = False
                    break
        
        if success:
            answer += 1
    
    return answer