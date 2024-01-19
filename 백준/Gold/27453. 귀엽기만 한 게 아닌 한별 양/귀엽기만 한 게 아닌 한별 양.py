from collections import deque
import sys
input = sys.stdin.readline
MAX = 10
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
maps = []
for i in range(N) :
  _maps = input().strip()
  for j in range(M) :
    if _maps[j] == 'S' :
      sx, sy = j, i
    if _maps[j] == 'H' :
      ex, ey = j, i
  maps.append(_maps)

visited = [[[False]*4 for _ in range(M)] for _ in range(N)]
q = deque([(sx, sy, -1, -1, 0, 0, 0)])
flg = False

while q :
  x, y, px, py, k0, k1, t = q.popleft()
  if x == ex and y == ey :
    flg = True
    break
  for i in range(4) :
    ax, ay = x + dx[i], y + dy[i]
    if -1 < ax < M and -1 < ay < N :
      if maps[ay][ax] == 'X' or (px, py) == (ax, ay) :
        continue
      new_k = 0 if maps[ay][ax] in 'SH' else int(maps[ay][ax])
      if k0 + k1 + new_k > K :
        continue
      if not visited[ay][ax][i] :
        visited[ay][ax][i] = True
        q.append((ax, ay, x, y, k1, new_k, t+1))
print(t if flg else -1)