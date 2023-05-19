from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def bfs(x, y) :
  visited[y][x] = True
  cnt = 1
  q = deque([(x, y)])
  while q :
    x, y = q.popleft()
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < m and -1 < ay < n and canvas[ay][ax] == 1 and not visited[ay][ax] :
        visited[ay][ax] = True
        q.append((ax, ay))
        cnt += 1

  return cnt

cnt = 0
result = 0
for i in range(n) :
  for j in range(m) :
    if canvas[i][j] == 1 and not visited[i][j] :
      cnt += 1
      result = max(result, bfs(j, i))
print(cnt)
print(result)