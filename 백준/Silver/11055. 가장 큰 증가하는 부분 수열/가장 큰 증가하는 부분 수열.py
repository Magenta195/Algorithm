N = int(input())
num_list = list(map(int, input().split()))
dp = [0]*N

def dfs(idx) :
  if dp[idx] > 0 :
    return dp[idx]
  
  dp[idx] = num_list[idx]
  for i in range(idx+1, N) :
    if num_list[i] > num_list[idx] :
      tmp = dfs(i)
      dp[idx] = max(dp[idx], num_list[idx] + tmp)

  return dp[idx]

for i in range(N) :
  dfs(i)
print(max(dp))