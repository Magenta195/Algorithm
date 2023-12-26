MOD = 10007
S = input().strip()
N = len(S)
dp = [[0]*N for _ in range(N)]
for i in range(N) :
  dp[i][i] = 1
for i in range(1, N) :
  for j in range(N-i) :
    dp[j][j+i] = (dp[j][j+i-1] + dp[j+1][j+i] - dp[j+1][j+i-1]) % MOD
    if S[j] == S[j+i] :
      dp[j][j+i] = (dp[j][j+i] + dp[j+1][j+i-1] + 1) % MOD
print(dp[0][-1])