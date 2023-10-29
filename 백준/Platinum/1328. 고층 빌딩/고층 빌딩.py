MOD = 1000000007
N, L, R = map(int, input().split())

dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[1][1][1] = 1

for i in range(1, N) :
  for j in range(1, i+1) :
    for k in range(1, i+1) :
      if not dp[i][j][k] :
        continue
      dp[i+1][j+1][k] += dp[i][j][k]
      dp[i+1][j][k+1] += dp[i][j][k]
      dp[i+1][j][k] += dp[i][j][k] * (i-1)

print(dp[N][L][R] % MOD)