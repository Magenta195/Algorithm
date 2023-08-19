import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
MAX = float('inf')
N = int(input())
W = int(input())
case_list = [list(map(int, input().split())) for _ in range(W)]
dp = [[[MAX, ''] for _ in range(W+1)] for _ in range(W+1)]

def dfs(idx1, idx2) :
  if idx1 == W or idx2 == W :
    return (0, 1)
  if dp[idx1][idx2][0] < MAX :
    return dp[idx1][idx2]

  nxt_idx = max(idx1, idx2) + 1
  nx, ny = case_list[nxt_idx-1]

  cx, cy = case_list[idx1-1] if idx1 > 0 else (1, 1)
  tmp, track = dfs(nxt_idx, idx2)
  tmp += abs(nx - cx) + abs(ny - cy)
  if tmp < dp[idx1][idx2][0] :
    dp[idx1][idx2] = (tmp, track * 2)
  
  cx, cy = case_list[idx2-1] if idx2 > 0 else (N, N)
  tmp, track = dfs(idx1, nxt_idx) 
  tmp += abs(nx - cx) + abs(ny - cy)
  if tmp < dp[idx1][idx2][0] :
    dp[idx1][idx2] = (tmp, track * 2 + 1)

  return dp[idx1][idx2]

result, track = dfs(0, 0)
print(result)
for i in range(W) :
  print(2 if track & (1 << i) else 1)