MOD = 1000000000
N = int(input())

dp = [1]*(N+1)
k = 2
while k <= N :
  for i in range(N - k + 1) :
    dp[i+k] = (dp[i+k] + dp[i])% MOD
  k *= 2
print(dp[-1])