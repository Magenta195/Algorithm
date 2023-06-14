import sys
input = sys.stdin.readline
MOD = 10007
N, M, H = map(int, input().split())
block_list = [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(H+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N) :
  for h in range(H+1) :
    if dp[i][h] :
      for j in block_list[i] :
        if h + j <= H :
          dp[i+1][h + j] = (dp[i][h] + dp[i+1][h + j] ) % MOD
print(dp[-1][-1])
