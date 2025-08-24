def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len_sec = (int(video_len.split(":")[0]) * 60) + int(video_len.split(":")[1])
    pos_sec = (int(pos.split(":")[0]) * 60) + int(pos.split(":")[1])
    op_start_sec = (int(op_start.split(":")[0]) * 60) + int(op_start.split(":")[1])
    op_end_sec = (int(op_end.split(":")[0]) * 60) + int(op_end.split(":")[1])
    
    for command in commands:
        # 10 초 전으로 이동
        if command == "prev":
            if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
                pos_sec = op_end_sec
            pos_sec = max(0, pos_sec - 10)    
        # 10 초 후로 이동
        elif command == "next":
            if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
                pos_sec = op_end_sec
            pos_sec = min(video_len_sec, pos_sec + 10)

        # 처음 오프닝 구간에 있는 경우
        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec
    
    answer = f"{(pos_sec // 60):02}:{pos_sec % 60:02}"
    
    return answer