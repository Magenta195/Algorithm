from collections import defaultdict
MAX = float('inf')

def calculate(n, req_list) :
    result = 0
    mento_list = [0]*(n+1)
    for a, b in req_list :
        best_mento, best_time = -1, MAX
        for i in range(n+1) :
            if best_time > mento_list[i] :
                best_mento, best_time = i, mento_list[i]
        result += max(0, best_time - a)
        mento_list[best_mento] = max(a, best_time) + b
    return result

def combs(left, idx):
    global req_dict, type_list, type_num
    if idx == type_num or not left :
        result = 0
        for i in range(type_num) :
            result += calculate(type_list[i], req_dict[i])
        return result
    
    result = MAX
    for i in range(left+1) :
        type_list[idx] = i
        result = min(result, combs(left-i, idx+1))
    type_list[idx] = 0
    return result

def solution(k, n, reqs):
    global req_dict, type_list, type_num
    type_num = k
    n -= k
    req_dict = defaultdict(list)
    type_list = [0]*k
    for a, b, c in reqs :
        req_dict[c-1].append((a, b))
    
    return combs(n, 0)