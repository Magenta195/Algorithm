MOD = 10007
N = int(input())
dp = [[0]*10 for _ in range(N)]

for i in range(N) :
  for j in range(10) :
    if i == 0 :
      dp[i][j] = 1
    else :
      for k in range(j+1) :
        dp[i][k] = (dp[i][k] + dp[i-1][j]) % MOD

print(sum(dp[-1]) % MOD)