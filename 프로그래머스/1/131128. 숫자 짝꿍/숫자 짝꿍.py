def solution(X, Y):
    cntX = dict()
    cntY = dict()
    
    for i in range(10):
        cntX[i] = X.count(str(i))
        cntY[i] = Y.count(str(i))
        
    answer = ''
    for i in range(9, -1, -1):
        cnt = min(cntX[i], cntY[i])
        if cnt == 0:
            continue
        answer += str(i)*cnt
    
    if answer == '':
        return '-1'
    if answer.count('0') == len(answer):
        return '0'
    return answer 