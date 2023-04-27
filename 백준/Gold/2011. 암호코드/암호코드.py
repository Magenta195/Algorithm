MOD = 1000000
N = input().strip()
if N == '0' :
  print(0)
  exit()
N_len = len(N)
dp = [0]*(N_len + 1)
dp[0] = 1
for i in range(N_len) :
  if N[i] == '0' :
    continue
  if i < N_len - 1 and '10' <= N[i:i+2] <= '26' :
    dp[i+2] = (dp[i+2] + dp[i]) % MOD
  dp[i+1] = (dp[i+1] + dp[i]) % MOD

print(dp[-1])