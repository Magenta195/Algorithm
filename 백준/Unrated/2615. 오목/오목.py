dx = [-1, 0, 1, 1]
dy = [1, 1, 0, 1]

N = 19
map_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[[False]*4 for _ in range(N)] for _ in range(N)]

def find_lines(x, y, r, target) :
  cnt = 0
  while -1 < x < N and -1 < y < N and map_list[y][x] == target and not visited[y][x][r]:
    cnt += 1
    visited[y][x][r] = True
    x, y = x + dx[r], y + dy[r]

  return cnt

def search():
  for i in range(N) :
    for j in range(N) :
      if map_list[i][j] > 0 :
        for k in range(4) :
          if find_lines(j, i, k, map_list[i][j]) == 5 :
            x, y = (j, i) if k > 0 else (j + dx[k]*4, i + dy[k]*4)
            return map_list[i][j], (x, y)

  return 0, (-1, -1)

def solve() :
  winner, (x, y) = search()
  print(winner)
  if winner > 0 :
    print(y+1, x+1)

solve()