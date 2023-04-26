N = int(input())
MOD = 1000000000
dp = [[0]*10 for _ in range(N)]

for i in range(1, 10) :
  dp[0][i] = 1

for i in range(1, N) :
  for j in range(10) :
    if j-1 >= 0 :
      dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
    if j+1 < 10 :
      dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD

print(sum(dp[-1]) % MOD)