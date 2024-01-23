from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]
MAX = 1000000

N = int(input())
houses = []
maps = []
for i in range(N) :
  _maps = input().strip()
  for j in range(N) :
    if _maps[j] == 'P' :
      houses.append((j, i))
      sx, sy = j, i
    if _maps[j] == 'K' :
      houses.append((j, i))
  maps.append(_maps)
height = [list(map(int, input().split())) for _ in range(N)]
min_range, max_range = set(), set()
rank = [height[y][x] for x, y in houses]
min_rank, max_rank = min(rank), max(rank)
for i in range(N) :
  for j in range(N) :
    if height[i][j] <= min_rank :
      min_range.add(height[i][j])
    if height[i][j] >= max_rank :
      max_range.add(height[i][j])

min_range = sorted(min_range)
max_range = sorted(max_range)
H = len(houses)

def bfs(minval, maxval) :
  q = deque([(sx, sy)])
  visited = [[False]*N for _ in range(N)]
  visited[sy][sx] = True
  cnt = 1
  while q :
    x, y = q.pop()
    for i in range(8) :
      ax, ay = x + dx[i], y + dy[i]
      if -1 < ax < N and -1 < ay < N and not visited[ay][ax] and minval <= height[ay][ax] <= maxval :
        visited[ay][ax] = True
        q.append((ax, ay))
        if maps[ay][ax] == 'K' :
          cnt += 1
    if cnt == H :
      return True
  return False

def two_pointer() :
  l, r = 0, 0
  ans = MAX+1
  while l < len(min_range) and r < len(max_range) :
    if bfs(min_range[l], max_range[r]) :
      ans = min(ans, max_range[r] - min_range[l])
      l += 1
    else :
      r += 1
  print(ans)

two_pointer()