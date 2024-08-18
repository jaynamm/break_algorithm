def solution(id_pw, db):
    answer = ''
    
    for acc in db:
        id = acc[0]
        pwd = acc[1]
        
        if id == id_pw[0] and pwd == id_pw[1]:
            answer = "login"
            break
        elif id == id_pw[0] and pwd != id_pw[1]:
            answer = "wrong pw"
            break
        else:
            answer = "fail"
    
    return answer