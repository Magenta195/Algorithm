MOD = 1000000000
N = int(input())

dp = [1]*(N+1)
k = 2
while k <= N :
  for i in range(k, N + 1) :
    dp[i] = (dp[i] + dp[i-k]) % MOD
  k *= 2
print(dp[-1])