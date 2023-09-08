from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX = float('inf')

N, M = map(int, input().split())
map_list = list()
C = list()
for i in range(N) :
  _map_list = input().strip()
  for j in range(M) :
    if _map_list[j] == 'S' :
      sx, sy = j, i
    if _map_list[j] == 'C' :
      C.append((j, i))
  map_list.append(_map_list)

q = deque()
visited = [[[[MAX]*4 for _ in range(4)] for _ in range(M)] for _ in range(N)]
for i in range(4) :
  q.append((sx, sy, i, 0, 0))
  visited[sy][sx][0][i] = 0
answer = MAX

while q :
  x, y, dir, c, dist = q.popleft()
  if c == 3 :
    answer = min(answer, dist)
    break
  for k in range(4) :
    if k == dir :
      continue
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ay < N and -1 < ax < M and map_list[ay][ax] != '#' :
      if map_list[ay][ax] == 'C' :
        ac = c | 2 if (ax, ay) == C[0] else c | 1
      else :
        ac = c
      if visited[ay][ax][ac][k] > dist + 1 :
        visited[ay][ax][ac][k] = dist + 1
        q.append((ax, ay, k, ac, dist+1))

print(answer if answer < MAX else -1)