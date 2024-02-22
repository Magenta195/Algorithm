MOD = 10**6 + 1
N = int(input())
M = int(input())
K = int(input())

dp = [[[0] * (K + 1) for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N+1) :
  for j in range(M+1) :
    dp[i][j][0] = 1

for k in range(1, K+1) :
  for i in range(1, N+1) :
    for j in range(1, M+1) :
      dp[i][j][k] = dp[i-1][j][k]
      dp[i][j][k] = (dp[i][j][k] + j * dp[i-1][j-1][k-1]) % MOD
      if k > 1 and j > 1 :
        dp[i][j][k] = (dp[i][j][k] + j * (j-1) * dp[i-1][j-2][k-2] // 2) % MOD
      if k > 1 and i > 1 :
        dp[i][j][k] = (dp[i][j][k] + j * (i-1) * dp[i-2][j-1][k-2]) % MOD

print(dp[-1][-1][-1])