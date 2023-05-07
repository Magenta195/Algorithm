MAX = 10001

dp = [0]*MAX
dp[0] = 1
for i in range(1, 4) :
  for j in range(MAX - i) :
    dp[j+i] += dp[j]

for _ in range(int(input())) :
  n = int(input())
  print(dp[n])