import sys
input = sys.stdin.readline

N = int(input())
wine_list = [int(input()) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]
dp[0][1] = dp[0][2] = wine_list[0]

for i in range(1, N) :
  dp[i][0] = max(dp[i-1])
  dp[i][1] = dp[i-1][0] + wine_list[i]
  dp[i][2] = dp[i-1][1] + wine_list[i]

print(max(dp[-1]))