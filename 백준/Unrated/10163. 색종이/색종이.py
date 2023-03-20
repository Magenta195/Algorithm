dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

MAX = 1001

N = int(input())
map_list = [[0]*MAX for _ in range(MAX)]

def fill() :
  for i in range(1, N+1) :
    _x, _y, w, h = map(int, input().split())
    for x in range(_x, _x+w) :
      for y in range(_y, _y+h) :
        map_list[y][x] = i

def dfs(x, y, target, visited) :
  q = [(x, y)]
  visited[y][x] = True
  cnt = 1

  while q :
    x, y = q.pop()

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < MAX and -1 < ay < MAX and map_list[ay][ax] == target and not visited[ay][ax] :
        cnt += 1
        visited[ay][ax] = True
        q.append((ax, ay))

  return cnt

def search() :
  paper_list = [0]*N
  visited = [[False]*MAX for _ in range(MAX)]
  for i in range(MAX) :
    for j in range(MAX) :
      if map_list[i][j] > 0 and not visited[i][j] :
        cnt = dfs(j, i, map_list[i][j], visited)
        paper_list[map_list[i][j]-1] += cnt

  return paper_list

def solve():
  fill()
  paper_list = search()
  for p in paper_list :
    print(p)

solve()