def solution(targets):
    if len(targets) == 1 :
        return 1
    
    answer = 1
    targets.sort(key = lambda x : (x[1], x[0]))
    prev_end = targets[0][1]
    for start, end in targets[1:] :
        if start >= prev_end :
            answer += 1
            prev_end = end
    
    return answer