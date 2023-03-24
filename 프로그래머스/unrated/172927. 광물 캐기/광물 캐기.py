mineral_dict = {
    'diamond' : 0,
    'iron' : 1,
    'stone' : 2
}
cost_mat = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]

def init(minerals) :
    minerals = [mineral_dict[mineral] for mineral in minerals]
    
    return minerals

def generate_mineral_list(minerals) :
    result = list()
    tmp = [0]*3
    for i in range(0, len(minerals), 5) :
        for j in range(5) :
            if i + j >= len(minerals) :
                break
            tmp[minerals[i+j]] += 1
        
        result.append(tmp)    
        tmp = [0]*3
        
    return result

def cal_cost(pick, mineral) :
    return sum([ cost_mat[pick][i] * mineral[i] for i in range(3) ])

def dfs(idx, picks, minerals, cost, max_idx) :
    if idx == max_idx :
        return cost
    
    result = float('inf')
    for i in range(3) :
        if picks[i] == 0 :
            continue
        picks[i] -= 1
        next_cost = cost + cal_cost(i, minerals[idx])
        result = min(result, dfs(idx+1, picks, minerals, next_cost, max_idx))
        picks[i] += 1
        
    return result

def solution(picks, minerals):
    minerals = init(minerals)
    minerals = generate_mineral_list(minerals)
    max_idx = min(sum(picks), len(minerals))
    answer = dfs(0, picks, minerals, 0, max_idx)
    return answer