def solution(today, terms, privacies):
    answer = []
    
    ty, tm, td = map(int, today.split("."))
    
    for i in range(1, len(privacies)+1):
        sdate, ptype = map(str, privacies[i-1].split())
        # 수집일자
        y, m, d = map(int, sdate.split("."))
        
        # 약관 종류 확인
        for term in terms:
            pt, exp = map(str, term.split(" "))
            
            # 약관 종류가 같으면
            if ptype == pt:
                m += int(exp)
        
        if 12 < m:
            y += m // 12
            if m % 12 == 0:
                y -= 1
                m = 12
            else:
                m = m % 12
                    
        print("today = ", ty, tm, td)
        print("exp = ", y, m, d)
        
        if y < ty:
            answer.append(i)
        elif y == ty and m < tm:
            answer.append(i)
        elif y == ty and m == tm and d <= td:
            answer.append(i)

    
    return answer