MAX = float('inf')
N = int(input())
map_list = list(map(int, input().split()))
dp = [MAX]*N
dp[0] = 0

for i in range(N) :
  if dp[i] == MAX :
    continue
  for j in range(map_list[i]) :
    if i+j+1 > N-1 :
      break
    dp[i+j+1] = min(dp[i+j+1], dp[i] + 1)

print(dp[-1] if dp[-1] < MAX else -1)