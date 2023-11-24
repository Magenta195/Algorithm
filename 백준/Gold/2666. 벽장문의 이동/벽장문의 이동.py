import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
f, s = sorted(map(int, input().split()))
T = int(input())
dp = [[[MAX]*(N+1) for _ in range(N+1)] for _ in range(T+1)]
dp[0][f][s] = 0

for i in range(T) :
  n = int(input())
  for f in range(1, N) :
    for s in range(f+1, N+1) :
      if dp[i][f][s] == MAX :
        continue
      if n < s :
        dp[i+1][n][s] = min(dp[i+1][n][s], dp[i][f][s] + abs(f - n))
      if n > f :
        dp[i+1][f][n] = min(dp[i+1][f][n], dp[i][f][s] + abs(n - s))

print(min(map(min, dp[-1])))