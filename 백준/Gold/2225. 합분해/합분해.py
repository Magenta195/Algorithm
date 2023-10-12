MOD = 10**9
N, K = map(int, input().split())

dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1

for i in range(1, K+1) :
  for j in range(N+1) :
    for k in range(j+1) :
      dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD

print(dp[-1][-1])
