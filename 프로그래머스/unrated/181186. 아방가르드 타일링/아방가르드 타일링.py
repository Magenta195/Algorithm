def solution(n):
    if n < 4 :
        return [0, 1, 3, 10][n]
    
    MOD = 1000000007
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 10

    partial_dp = [10, 1, 3]
    dp_sum = sum(partial_dp)
    
    for i in range(4, n+1) :
        _add = 2 if i % 3 else 4
        dp[i] = (dp_sum*2 % MOD - dp[i-1] + partial_dp[i%3]* 2 % MOD + dp[i-3] + _add) % MOD
        dp_sum = (dp_sum + dp[i]) % MOD
        partial_dp[i%3] = (partial_dp[i%3] + dp[i]) % MOD

    return dp[n]