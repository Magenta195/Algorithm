N = int(input())
dp = [0]*(N+1)
dp[0] = 1
for i in range(2, N+1, 2) :
  for j in range(2, i+1, 2) :
    mul = 3 if j == 2 else 2
    dp[i] += dp[i-j] * mul
print(dp[-1])