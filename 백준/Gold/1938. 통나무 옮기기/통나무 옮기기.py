from collections import deque
import sys 
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
drx = [[-1, 0, 1], [0, 0, 0]]
dry = [[0, 0, 0], [-1, 0, 1]]

N = int(input())
map_list, B_list, E_list = list(), list(), list()

for i in range(N) :
  _map_list = input().strip()
  for j in range(N) :
    if _map_list[j] == 'E' :
      E_list.append((j, i))
    if _map_list[j] == 'B' :
      B_list.append((j, i))
  map_list.append(_map_list)

bx = (B_list[0][0] + B_list[1][0] + B_list[2][0]) // 3
by = (B_list[0][1] + B_list[1][1] + B_list[2][1]) // 3
br = 0 if B_list[0][0] != B_list[1][0] else 1

ex = (E_list[0][0] + E_list[1][0] + E_list[2][0]) // 3
ey = (E_list[0][1] + E_list[1][1] + E_list[2][1]) // 3
er = 0 if E_list[0][0] != E_list[1][0] else 1

q = deque([(bx, by, br, 0)])
visited = [[[False]*2 for _ in range(N)] for _ in range(N)]
visited[by][bx][br] = True

while q :
  x, y, r, dist = q.popleft()
  if (x, y, r) == (ex, ey, er) :
    print(dist)
    exit()
    
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    flg = False
    for i in range(3) :
      arx, ary = ax + drx[r][i], ay + dry[r][i]
      if not (-1 < arx < N and -1 < ary < N and map_list[ary][arx] != '1') :
        flg = True
        break
    if flg or visited[ay][ax][r]:
      continue
    visited[ay][ax][r] = True
    q.append((ax, ay, r, dist+1))

  flg = False
  r = 1-r
  for ay in [y-1, y, y+1] :
    for ax in [x-1, x, x+1] :
      if not (-1 < ay < N and -1 < ax < N and map_list[ay][ax] != '1') :
        flg = True
        break
    if flg :
      break
  if flg or visited[y][x][r]:
    continue
  visited[y][x][r] = True
  q.append((x, y, r, dist+1))
print(0)