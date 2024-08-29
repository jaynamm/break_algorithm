def solution(plans):
    answer = []
    # 입력 데이터 전처리: 시작 시간 기준으로 정렬
    plans.sort(key=lambda x: x[1])
    
    running = []  # 진행 중인 일정들을 저장할 스택
    current_time = 0  # 현재 시간
    
    for plan in plans:
        name, start, playtime = plan
        
        # 시간을 분으로 변환
        start = int(start[:2]) * 60 + int(start[3:])  
        playtime = int(playtime)
        
        # 스택에 있는 일정 처리
        while running and current_time + running[-1][1] <= start:
            last_name, last_playtime = running.pop()
            current_time += last_playtime
            answer.append(last_name)
        
        # 스택에 남은 일정의 남은 시간을 업데이트
        if running:
            running[-1][1] -= (start - current_time)
        
        # 새로운 일정 스택에 추가
        running.append([name, playtime])
        current_time = start
    
    # 스택에 남은 일정 처리
    while running:
        answer.append(running.pop()[0])
    
    return answer
