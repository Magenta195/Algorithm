from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fire_bfs(q_list) :
  visited = [[float('inf')]*M for _ in range(N)]
  q = deque()
  for x, y in q_list :
    q.append((x, y, 0))
    visited[y][x] = 0

  while q :
    x, y, dist = q.popleft()

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N and map_list[ay][ax] != '#' and visited[ay][ax] > dist+1 :
        visited[ay][ax] = dist + 1
        q.append((ax, ay, dist+1))

  return visited
        
def man_bfs(x, y, visited) :
  q = deque([(x, y, 0)])
  visited[y][x] = 0
  while q :
    x, y, dist = q.popleft()

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N :
        if map_list[ay][ax] != '#' and visited[ay][ax] > dist+1 :
          visited[ay][ax] = dist + 1
          q.append((ax, ay, dist+1))
      else :
        return dist+1

  return -1


T = int(input())
for _ in range(T) :
  M, N = map(int, input().split())
  map_list = [input().strip() for _ in range(N)]

  fire_list = list()
  for i in range(N) :
    for j in range(M) :
      if map_list[i][j] == '*' :
        fire_list.append((j, i))
      elif map_list[i][j] == '@' :
        x, y = j, i

  visited = fire_bfs(fire_list)
  result = man_bfs(x, y, visited)

  print(result if result > -1 else 'IMPOSSIBLE')

