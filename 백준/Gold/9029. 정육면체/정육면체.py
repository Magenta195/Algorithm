import sys
input = sys.stdin.readline
MAX = float('inf')

dp = [[[MAX for k in range(201)] for i in range(201)] for j in range(201)]
for i in range(1, 201) :
  for j in range(1, 201) :
    for k in range(1, 201) :
      if dp[i][j][k] < MAX :
        continue
      if i == j == k :
        dp[i][j][k] = 1
      elif i % k == j % k == 0 :
        dp[i][j][k] = (i // k)*(j // k)
      elif i % j == k % j == 0 :
        dp[i][j][k] = (i // j)*(k // j)
      elif j % i == k % i == 0 :
        dp[i][j][k] = (j // i)*(k // i)
      else :
        for l in range(1, max(i, j, k) // 2 + 1) :
          if l <= i // 2 :
            dp[i][j][k] = min(dp[i][j][k], dp[l][j][k] + dp[i-l][j][k])
          if l <= j // 2 :
            dp[i][j][k] = min(dp[i][j][k], dp[i][l][k] + dp[i][j-l][k])
          if l <= k // 2 :
            dp[i][j][k] = min(dp[i][j][k], dp[i][j][l] + dp[i][j][k-l])
      dp[i][k][j] = dp[j][i][k] = dp[j][k][i] = dp[k][j][i] = dp[k][i][j] = dp[i][j][k]


def solve() :
  W, L, H = map(int, input().split())
  print(dp[W][L][H])

for _ in range(int(input())) :
  solve()