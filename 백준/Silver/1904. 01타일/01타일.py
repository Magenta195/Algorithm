N = int(input())
if N == 1 :
  print(1)
  exit()
dp = [0]*N
dp[0], dp[1] = 1, 2

for i in range(2, N) :
  dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[-1])