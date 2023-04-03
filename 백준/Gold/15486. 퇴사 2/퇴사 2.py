import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)

for idx in range(N) :
  t, p = map(int, input().split())
  if idx+t <= N :
    dp[idx+t] = max(dp[idx+t], dp[idx] + p)
  dp[idx+1] = max(dp[idx+1], dp[idx])

print(dp[-1])