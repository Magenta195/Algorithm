import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
pad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0, -1, -1]
]
MOD = 1234567
MAX = 1001
dp = [[0]*10 for _ in range(MAX)]

for i in range(10) :
  dp[1][i] = 1

for i in range(1, MAX-1) :
  for j in range(10) :
    if j == 0:
      x, y = 0, 3
    else :
      x, y = (j-1) % 3, (j-1) // 3

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < 3 and -1 < ay < 4 and pad[ay][ax] > -1 :
        dp[i+1][pad[ay][ax]] = (dp[i+1][pad[ay][ax]] + dp[i][j]) % MOD

T = int(input())
for _ in range(T) :
  n = int(input())
  print(sum(dp[n]) % MOD)