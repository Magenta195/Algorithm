from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, visited) :
  q = deque([(x, y)])
  visited[y][x] = True
  removed_list = list()
  
  while q :
    x, y = q.popleft()
    adj_zeros = 0
    for k in range(4) :
      ax, ay = x+dx[k], y+dy[k]
      if -1 < ax < M and -1 < ay < N :
        if map_list[ay][ax] > 0 and not visited[ay][ax] :
          visited[ay][ax] = True
          q.append((ax, ay))
        elif map_list[ay][ax] == 0 :
          adj_zeros += 1

    if adj_zeros :
      removed_list.append((x, y, adj_zeros))

  return removed_list

def search() :
  bfs_cnt = 0
  visited = [[False]*M for _ in range(N)]
  removed_list = list()
  
  for i in range(N) :
    for j in range(M) :
      if map_list[i][j] > 0 and not visited[i][j] :
        removed_list.extend(bfs(j, i, visited))
        bfs_cnt += 1

  for x, y, adj_zeros in removed_list :
    map_list[y][x] = max(map_list[y][x] - adj_zeros, 0)

  return bfs_cnt

def solve() :
  t = 1
  while True :
    bfs_cnt = search()
    if bfs_cnt >= 2 :
      return t-1
    if bfs_cnt == 0 :
      return 0
    t += 1

print(solve())
    
  