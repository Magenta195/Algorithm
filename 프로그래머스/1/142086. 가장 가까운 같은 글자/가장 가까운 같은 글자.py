def solution(s):
    answer = []
    last_visit = dict()
    
    for i, _s in enumerate(s):
        if _s not in last_visit :
            answer.append(-1)
        else :
            answer.append(i-last_visit[_s])
        last_visit[_s] = i
    return answer