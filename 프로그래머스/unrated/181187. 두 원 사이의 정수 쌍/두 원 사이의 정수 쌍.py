from math import ceil, floor

def solution(r1, r2):
    answer = (r2 - r1 + 1) * 4
    for y in range(1, r2):
        maxval = floor((r2**2 - y**2) ** 0.5)
        if r1 <= y :
            minval = 1
        else :
            minval = ceil((r1**2 - y**2) ** 0.5)
        answer += 4*(maxval - minval + 1)
            
    return answer