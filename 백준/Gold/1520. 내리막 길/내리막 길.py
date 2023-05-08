import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]
dp[-1][-1] = 1

def dfs(x, y):
  if dp[y][x] > -1 :
    return dp[y][x]

  dp[y][x] = 0
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < N and -1 < ay < M and map_list[y][x] > map_list[ay][ax] :
      dp[y][x] += dfs(ax, ay)

  return dp[y][x]

print(dfs(0, 0))