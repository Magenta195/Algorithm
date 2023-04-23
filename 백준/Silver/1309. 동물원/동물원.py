N = int(input())
MOD = 9901
dp = [[0]*3 for _ in range(N)]
dp[0][0] = dp[0][1] = dp[0][2] = 1

for i in range(N-1) :
  for j in range(3) :
    if j == 0 :
      _range = range(1, 4)
    else :
      _range = range(1, 3)
    for k in _range :
      dp[i+1][(j+k) % 3] = (dp[i+1][(j+k) % 3] + dp[i][j]) % MOD

print(sum(dp[-1]) % MOD)

