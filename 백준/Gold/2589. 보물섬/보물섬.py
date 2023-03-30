
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def init() :
  global N, M
  N, M = map(int, input().split())
  map_list = [input().strip() for _ in range(N)]

  return map_list

def bfs(x, y, map_list) :
  global N, M
  visited = [[False]*M for _ in range(N)]

  q = deque([(x, y, 0)])
  visited[y][x] = True

  max_dist = 0
  while q :
    x, y, dist = q.popleft()
    max_dist = max(dist, max_dist)
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N and map_list[ay][ax] == 'L' and not visited[ay][ax] :
        visited[ay][ax] = True
        q.append((ax, ay, dist+1))

  return max_dist

def search(map_list) :
  result = 0
  for i in range(N) :
    for j in range(M) :
      if map_list[i][j] == 'L' :
        result = max(result, bfs(j, i, map_list))

  print(result)

def solve() :
  map_list = init()
  search(map_list)

solve()