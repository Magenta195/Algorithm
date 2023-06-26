import sys
sys.setrecursionlimit(100000)

N = int(input())
left_list = [1, 3, 4]
dp = [-1]*(N+1)
dp[0] = True
def dfs(left) :
  if not left :
    return False
  if dp[left] != -1 :
    return dp[left]
    
  result = True
  for _left in left_list :
    if left - _left < 0 :
      continue
    result &= dfs(left - _left)

  dp[left] = not result
  return dp[left]

print("SK" if dfs(N) else "CY")