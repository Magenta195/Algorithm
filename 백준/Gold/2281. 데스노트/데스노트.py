import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
name_list = [int(input()) for _ in range(n)]

dp = [[-1]*n for _ in range(n)]

def dfs(line, idx) :
  if idx == n :
    return 0
  if dp[line][idx] > -1 :
    return dp[line][idx]
  if sum(name_list[idx:]) + (n - idx) - 1 <= m :
    dp[line][idx] = 0
    return 0
  
  dp[line][idx] = float('inf')
  next_idx = idx
  left = m
  while next_idx < n and left >= name_list[next_idx] :
    left -= name_list[next_idx]
    dp[line][idx] = min(dp[line][idx], left ** 2 + dfs(line+1, next_idx+1))
    left -= 1
    next_idx += 1

  return dp[line][idx]

print(dfs(0, 0))
