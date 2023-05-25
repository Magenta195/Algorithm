from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
R, C = map(int, input().split())
map_list = [list(input().strip()) for _ in range(R)]

water_q = deque()
swan_q = deque()
swan_visited = [[False]*C for _ in range(R)]
water_visited = [[False]*C for _ in range(R)]
for i in range(R) :
  for j in range(C) :
    if map_list[i][j] == 'L' :
      water_visited[i][j] = True
      water_q.append((i, j))
      if not swan_q :
        swan_visited[i][j] = True
        swan_q.append((i, j))
      else :
        tr, tc = i, j
      map_list[i][j] = '.'
    elif map_list[i][j] == '.' :
      water_visited[i][j] = True
      water_q.append((i, j))

flg = True
cnt = 0
while True :
  next_swan_q = deque()
  next_water_q = deque()
  while water_q :
    r, c = water_q.popleft()
    if map_list[r][c] == 'X' :
      map_list[r][c] = '.'
    for k in range(4) :
      ar, ac = r + dr[k], c + dc[k]
      if -1 < ar < R and -1 < ac < C and not water_visited[ar][ac] :
        water_visited[ar][ac] = True
        if map_list[ar][ac] == 'X' : 
          next_water_q.append((ar,ac))
        else :
          water_q.append((ar, ac))
  while swan_q :
    r, c = swan_q.popleft()
    if r == tr and c == tc :
      flg = False
      break
    for k in range(4) :
      ar, ac = r + dr[k], c + dc[k]
      if -1 < ar < R and -1 < ac < C and not swan_visited[ar][ac] :
        swan_visited[ar][ac] = True
        if map_list[ar][ac] in '.' :
          swan_q.append((ar, ac))
        else :
          next_swan_q.append((ar, ac))
  if not flg : 
    break
  swan_q = next_swan_q
  water_q = next_water_q
  cnt += 1
print(cnt)