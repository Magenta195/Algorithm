dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
source_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def search(start) :
  result = 0
  for idx in range(start, N*M) :
    i, j = idx // M, idx % M
    if not visited[i][j] :
      nxt = i * M + j
      tmp = dfs(nxt)
      if tmp > result :
        result = tmp
  return result

def dfs(start) :
  result = 0
  x, y = start % M, start // M
  visited[y][x] = True
  for a in range(4) :
    ax, ay = x + dx[a], y + dy[a]
    if not (-1 < ax < M and -1 < ay < N) or visited[ay][ax] :
      continue
    b = (a + 1) % 4
    bx, by = x + dx[b], y + dy[b]
    if not (-1 < bx < M and -1 < by < N) or visited[by][bx] :
      continue
    next = start + 1 if a < 2 else start + 2
    visited[ay][ax] = visited[by][bx] = True
    tmp = search(next) + source_list[y][x]*2 + source_list[ay][ax] + source_list[by][bx]
    if tmp > result :
      result = tmp
    visited[ay][ax] = visited[by][bx] = False
  visited[y][x] = False
  return result

print(search(0))