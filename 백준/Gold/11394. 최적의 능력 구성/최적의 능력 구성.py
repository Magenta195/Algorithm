import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(1 << N)
skills = [list(map(int, input().split())) for _ in range(N)]

for i in range(N) :
  dp[1 << i] = skills[i][0] / 100 * skills[i][1]

for i in range(1, 1 << N) :
  dp[i] /= bin(i).count('1')
  for j in range(N) :
    if i & (1 << j) :
      continue
    dp[i | (1 << j)] += dp[1 << j] + (100 - skills[j][0]) / 100 * dp[i]
print(max(dp))