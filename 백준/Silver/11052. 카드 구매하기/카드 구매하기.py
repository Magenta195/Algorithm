N = int(input())
p_list = list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(N) :
  for j in range(N-i) :
    dp[j+i+1] = max(dp[j+i+1], dp[j] + p_list[i])

print(dp[-1])