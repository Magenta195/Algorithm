import sys
input = sys.stdin.readline

MAX = float('inf')
T, W = map(int, input().split())
dp = [[[-MAX]*(W+1) for _ in range(2)] for _ in range(T+1)]
dp[0][0][W] = dp[0][1][W-1] = 0
for t in range(T) :
  idx = int(input()) - 1
  for i in range(2) :
    for w in range(W+1) :
      if idx == i :
        dp[t+1][i][w] = max(dp[t+1][i][w], dp[t][i][w]+1)
      elif w > 0 :
        dp[t+1][1-i][w-1] = max(dp[t+1][1-i][w-1], dp[t][i][w]+1)
      dp[t+1][i][w] = max(dp[t+1][i][w], dp[t][i][w])

print(max(map(max, dp[-1])))
  