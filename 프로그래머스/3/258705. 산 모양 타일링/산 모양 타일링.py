MOD = 10007

def solution(n, tops):
    dp = [[0]*2 for _ in range(n)]
    if tops[0] :
        dp[0][0] = 3
        dp[0][1] = 1
    else :
        dp[0][0] = 2
        dp[0][1] = 1
    
    for i in range(1, n) :
        mul = [(3, 2), (1, 1)] if tops[i] else [(2, 1), (1, 1)]
        for j in range(2) :
            dp[i][j] = (dp[i][j] + dp[i-1][0]*mul[j][0] + dp[i-1][1]*mul[j][1]) % MOD
    
    return sum(dp[-1]) % MOD