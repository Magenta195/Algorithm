from collections import deque
import sys
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
cave_list = [list(input().strip()) for _ in range(R)]
N = int(input())
throw_list = list(map(int, input().split()))

def throw(r, order) :
  if order % 2 :
    _range = range(C-1, -1, -1)
  else :
    _range = range(C)
  for i in _range :
    if cave_list[r][i] == 'x' :
      cave_list[r][i] = '.'
      return True
  return False

def bfs(r, c, visited) :
  visited[r][c] = True
  visited_coord = [[r, c]]
  q = deque(visited_coord)
  while q :
    r, c = q.popleft()
    for k in range(4) :
      ar, ac = r + dr[k], c + dc[k]
      if -1 < ar < R and -1 < ac < C and not visited[ar][ac] and cave_list[ar][ac] == 'x' :
        visited[ar][ac] = True
        visited_coord.append([ar, ac])
        q.append((ar, ac))
  return visited_coord

def cluster_move(visited_coord) :
  for r, c in visited_coord :
    cave_list[r][c] = '.'
  flg = True
  i = 0
  while flg :
    i += 1
    for r, c in visited_coord :
      if r+i >= R or cave_list[r+i][c] == 'x' :
        flg = False
        break
        
  for r, c in visited_coord :
    cave_list[r+i-1][c] = 'x'

def cluster_search() :
  visited = [[False]*C for _ in range(R)]
  visited_coord = list()
  for i in range(C) :
    if not visited[-1][i] and cave_list[-1][i] == 'x' :
      bfs(R-1, i, visited)
  for i in range(R-1) :
    for j in range(C) :
      if not visited[i][j] and cave_list[i][j] == 'x' :
        visited_coord = bfs(i, j, visited)
        break
    if visited_coord :
      break
  if visited_coord :
    cluster_move(visited_coord)

for n in range(N) :
  is_movable = throw(R-throw_list[n], n)
  if is_movable :
    cluster_search()

for _cave in cave_list :
  print(''.join(_cave))