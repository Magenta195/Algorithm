from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
map_list = [list(map(int, input().strip())) for _ in range(N)]
result = 0

def bfs(x, y) :
  q = deque([(x, y)])

  init_val = map_list[y][x]
  min_border = 10
  result = set()
  result.add((x, y))
  while q :
    x, y = q.popleft()
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if not (-1 < ax < M and -1 < ay < N) :
        return 0, set()
      if map_list[ay][ax] <= init_val and (ax, ay) not in result :
        result.add((ax, ay))
        q.append((ax, ay))
      elif map_list[ay][ax] > init_val :
        min_border = min(min_border, map_list[ay][ax])

  return min_border, result

def fill(val, coord_set) :
  global result
  for x, y in coord_set :
    result += val - map_list[y][x]
    map_list[y][x] = val

for i in range(N) :
  for j in range(M) :
    val, coord_set = bfs(j, i)
    if coord_set :
      fill(val, coord_set)

print(result)