def solution(schedules, timelogs, startday):
    answer = 0
    
    # 일한 직원의 수
    workers = len(schedules)
    
    # 요일 계산
    day_of_weeks = [(startday + i - 1) % 7 + 1 for i in range(0, 7)]
    print(day_of_weeks)
            
    # 각 직원마다 출근 여부 확인
    for i in range(workers):
        # 성공 여부
        success = True
        
        # 출근 데드라인
        deadline = schedules[i] + 10
        
        # 만약 10분을 더한 시각이 60분을 넘어가면 + 1시간을 해주어야 한다.
        if deadline % 100 > 59:
            deadline += 100
            deadline -= 60
        
        # 각 직원마다 시간 기록을 가져온다.
        for j in range(len(timelogs[i])):
            # 만약 토요일(6), 일요일(7) 이라면 넘어간다.
            if day_of_weeks[j] in [6, 7]:
                continue
            else:
                # deadline 보다 늦었다면 이벤트 실패
                if timelogs[i][j] > deadline:
                    success = False
                    break
        # 성공하면 상품을 받을 수 있다.        
        if success:
            answer += 1
    
    return answer