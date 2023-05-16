import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
name_list = [int(input()) for _ in range(n)]
MAX = float('inf')
dp = [MAX]*(n+1)
dp[n] = 0

def dfs(idx) :
  if dp[idx] < MAX :
    return dp[idx]

  left = m - name_list[idx]
  next_idx = idx+1
  while next_idx <= n and left >= 0 :
    if next_idx == n :
      dp[idx] = 0
      break
    dp[idx] = min(dp[idx], left ** 2 + dfs(next_idx))
    left -= 1 + name_list[next_idx]
    next_idx += 1

  return dp[idx]

print(dfs(0))