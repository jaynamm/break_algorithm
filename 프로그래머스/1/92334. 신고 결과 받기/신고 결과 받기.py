def solution(id_list, report, k):
    answer = []
    
    # 자신을 신고한 사람을 저장하기 위한 dict : {"신고받은 사람" : {신고한 사람}}
    # set 을 사용해서 중복을 제거해준다.
    report_user_by_id = {id: set() for id in id_list}
    # 유저마다 받는 메일을 세어준다.
    reported_count_by_id = {id: 0 for id in id_list}
    
    for r in report:
        reporter, reported_user = r.split()
        report_user_by_id[reported_user].add(reporter)
    
    for id in id_list:
        # id 마다 신고 당한 횟수 가져오기    
        # 신고받은 횟수가 2회 이상이면 정지 -> 신고한 사람이 메일을 받음
        if len(report_user_by_id[id]) >= k:
            # 신고한 사람의 메일 개수를 증가시켜준다.
            for user in report_user_by_id[id]:
                reported_count_by_id[user] += 1
                
    # id_list 순서에 맞춰준다.
    answer = [reported_count_by_id[id] for id in id_list]
    
    return answer