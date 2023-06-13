from collections import defaultdict, deque
import sys
input = sys.stdin.readline
cvt = lambda x : int(x)-1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

switch_dict = defaultdict(list)
for _ in range(M) :
  x, y, a, b = map(cvt, input().split())
  switch_dict[(x, y)].append((a, b))

enable = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
enable[0][0] = 1
visited[0][0] = True
q = deque([(0, 0)])

while q :
  x, y = q.popleft()

  for _x, _y in switch_dict[(x, y)] :
    if not enable[_y][_x] :
      enable[_y][_x] = 1
      if visited[_y][_x] :
        q.append((_x, _y))

  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < N and -1 < ay < N and not visited[ay][ax] :
      visited[ay][ax] = True
      if enable[ay][ax] :
        q.append((ax, ay))

print(sum(map(sum, enable)))