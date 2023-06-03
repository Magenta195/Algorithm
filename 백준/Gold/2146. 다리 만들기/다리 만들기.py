from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
MAX = float('inf')
N = int(input())

map_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*N for _ in range(N)]
land_q = list()
cnt = 0

def bfs(x, y) :
  global cnt
  q = deque([(x, y)])
  _land_q = deque([(x, y, 0)])
  visited[y][x] = cnt
  while q :
    x, y = q.popleft()
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < N and -1 < ay < N and map_list[ay][ax] == 1 and visited[ay][ax] == -1 :
        visited[ay][ax] = cnt
        q.append((ax, ay))
        _land_q.append((ax, ay, 0))
  land_q.append(_land_q)
  cnt += 1

def land_bfs(num) :
  land_visited = [[MAX]*N for _ in range(N)]
  _land_q = land_q[num]
  for x, y, _ in _land_q :
    land_visited[y][x] = 0
  while _land_q :
    x, y, dist = _land_q.popleft()
    if visited[y][x] > num :
      return dist
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < N and -1 < ay < N and land_visited[ay][ax] > dist + 1 :
        land_visited[ay][ax] = dist + 1
        _land_q.append((ax, ay, dist + 1))
  return MAX

for i in range(N) :
  for j in range(N) :
    if visited[i][j] == -1 and map_list[i][j] == 1 :
      bfs(j, i)

result = MAX
for i in range(cnt) :
  result = min(result, land_bfs(i)-1)
print(result)