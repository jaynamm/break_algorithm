def solution(emergency):
    em = {e:i+1 for i, e in enumerate(sorted(emergency, reverse=True))}
    
    return [em[e] for e in emergency]