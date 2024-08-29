def solution(plans):
    result = []
    # 입력 데이터 전처리: 시작 시간 기준으로 정렬
    plans.sort(key=lambda x: x[1])
    
    stack = []  # 진행 중인 일정들을 저장할 스택
    current_time = 0  # 현재 시간
    
    for plan in plans:
        name, start_time, duration = plan
        start_time = int(start_time[:2]) * 60 + int(start_time[3:])  # 시간을 분으로 변환
        duration = int(duration)
        
        # 스택에 있는 일정 처리
        while stack and current_time + stack[-1][1] <= start_time:
            last_name, last_duration = stack.pop()
            current_time += last_duration
            result.append(last_name)
        
        # 스택에 남은 일정의 남은 시간을 업데이트
        if stack:
            stack[-1][1] -= (start_time - current_time)
        
        # 새로운 일정 스택에 추가
        stack.append([name, duration])
        current_time = start_time
    
    # 스택에 남은 일정 처리
    while stack:
        result.append(stack.pop()[0])
    
    return result
