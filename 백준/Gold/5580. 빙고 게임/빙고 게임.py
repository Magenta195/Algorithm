MOD = 100000
N, M, S= map(int, input().split())
dp = [[0]*(S+1) for _ in range(N**2+1)]
dp[0][0] = 1
for i in range(1, M+1) :
  for j in range(N**2, -1, -1) :
    for k in range(i, S+1) :
      dp[j][k] = (dp[j][k] + dp[j-1][k-i]) % MOD
print(dp[-1][-1] % MOD)