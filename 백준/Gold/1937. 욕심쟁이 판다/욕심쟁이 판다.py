import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

def dfs(x, y) :
  if dp[y][x] > 0 :
    return dp[y][x]

  dp[y][x] = 1
  for k in range(4) :
    ax, ay = x + dx[k] ,y + dy[k]
    if -1 < ax < N and -1 < ay < N and map_list[ay][ax] > map_list[y][x] :
      dp[y][x] = max(dp[y][x], dfs(ax, ay) + 1)

  return dp[y][x]

for i in range(N) :
  for j in range(N) :
    dfs(j, i)

print(max(map(max, dp)))