import sys
input = sys.stdin.readline

dx = [1, 0]
dy = [0, 1]

N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(N)]
dp[-1][-1] = 1

def dfs(x, y) :
  if dp[y][x] > -1 :
    return dp[y][x]
  if map_list[y][x] == 0 :
    return 0
  dp[y][x] = 0
  for k in range(2) :
    ax, ay = x + map_list[y][x]*dx[k], y + map_list[y][x]*dy[k]
    if -1 < ax < N and -1 < ay < N :
      dp[y][x] += dfs(ax, ay)
  return dp[y][x]

print(dfs(0, 0))