from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N, M = map(int, input().split())
visited = [[float('inf')]*M for _ in range(N)]
map_list = list()
q = deque()
for i in range(N) :
  _map_list = list(map(int, input().split()))
  for j in range(M) :
    if _map_list[j] == 2 :
      visited[i][j] = 0
      q.append((j, i, 0))
    elif _map_list[j] == 0 :
      visited[i][j] = 0
  map_list.append(_map_list)

while q :
  x, y, dist = q.popleft()

  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < M and -1 < ay < N and map_list[ay][ax] == 1 and visited[ay][ax] > dist + 1 :
      visited[ay][ax] = dist + 1
      q.append((ax, ay, dist+1))

for i in range(N) :
  for j in range(M) :
    if visited[i][j] == float('inf') :
      visited[i][j] = -1

for _visited in visited :
  print(*_visited)