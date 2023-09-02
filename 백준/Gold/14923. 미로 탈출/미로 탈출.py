from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cvt = lambda x : int(x)-1
N, M = map(int, input().split())
hx, hy = map(cvt, input().split())
ex, ey = map(cvt, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
visited[hx][hy][0] = True
q = deque([(hy, hx, 0, 0)])
while q :
  x, y, move, wand = q.popleft()
  if (ey, ex) == (x, y) :
    print(move)
    exit()

  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < M and -1 < ay < N :
      if maps[ay][ax] == 0 and not visited[ay][ax][wand] :
        visited[ay][ax][wand] = True
        q.append((ax, ay, move+1, wand))
      if maps[ay][ax] == 1 and not wand and not visited[ay][ax][1] :
        visited[ay][ax][1] = True
        q.append((ax, ay, move+1, 1))
print(-1)