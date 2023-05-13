import sys
input = sys.stdin.readline

MAX = 1000001
MOD = 1000000009
dp = [0]*MAX
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, MAX) :
  dp[i] = dp[i-1]%MOD + dp[i-2]%MOD + dp[i-3]%MOD

for _ in range(int(input())) :
  print(dp[int(input())]%MOD)