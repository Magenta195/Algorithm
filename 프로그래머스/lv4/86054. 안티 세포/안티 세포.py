def get_dp(a, s):
    i = 1
    ct = 1
    record = [{} for _ in range(s)]
    record[0][a[0]] = (1,None)
    
    while i < s:
        record[i][a[i]] = (ct,i-1)
        var = a[i]
        j = i-1
        while record[j].get(var,None)!=None:
            diff = record[j][var]
            ct += diff[0]
            var *= 2
            record[i][var] = diff
            j = diff[1]
            if j == None:
                break
        i+=1
    return ct%(10**9 + 7)

def solution(a, s):
    answer = []
    a_idx = 0
    for _s in s:
        result = get_dp(a[a_idx:a_idx+_s], _s)
        a_idx += _s
        answer.append(result)
    return answer