MOD = 100030001
N, L = map(int, input().split())

sum_dp = [0]*(N+1)
last_dp = [0]*(N+1)
sum_dp[0] = last_dp[1] = 1

for i in range(L-1) :
  new_dp = [0]*(N+1)
  for j in range(i+1, N+1) :
    for k in range(N+1) :
      if j + k + 1 > N :
        break
      new_dp[j+k+1] = (new_dp[j+k+1] + 2 * last_dp[j] * sum_dp[k]) % MOD
      new_dp[j+k+1] = (new_dp[j+k+1] + last_dp[j] * last_dp[k]) % MOD
  for j in range(N+1) :
    sum_dp[j] = (sum_dp[j] + last_dp[j]) % MOD
  last_dp = new_dp

print(last_dp[-1])