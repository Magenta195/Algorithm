N = int(input())
n_list = list(map(int, input().split()))

dp = [[-float('inf')]*2 for _ in range(N)]
dp[0][0] = n_list[0]
dp[0][1] = n_list[0]
for i in range(1, N) :
  dp[i][0] = max(dp[i-1])
  dp[i][1] = max(dp[i-1][1] + n_list[i], n_list[i])

print(max(map(max, dp)))