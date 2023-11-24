from heapq import heappush, heappop

def solution(alp, cop, problems):
    answer = 0
    MAX = float('inf')
    
    max_cop, max_alp = 0, 0
    for alp_req, cop_req, _, _, _ in problems :
        max_cop = max(max_cop, cop_req)
        max_alp = max(max_alp, alp_req)
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    dp = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    q = [(0, alp, cop)]
    
    while q :
        t_acq, alp_acq, cop_acq = heappop(q)
        alp_acq = min(alp_acq, max_alp)
        cop_acq = min(cop_acq, max_cop)
        if t_acq >= dp[alp_acq][cop_acq] :
            continue
        if alp_acq == max_alp and cop_acq == max_cop :
            dp[max_alp][max_cop] = t_acq
            break

        dp[alp_acq][cop_acq] = t_acq
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
            if alp_req <= alp_acq and cop_req <= cop_acq :
                heappush(q, (t_acq+cost, alp_acq+alp_rwd, cop_acq+cop_rwd))
                
    return dp[-1][-1]