from collections import deque

MAX = float('inf')
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
map_list = [list(input().strip()) for _ in range(N)]

door_list = ['A', 'B', 'C', 'D', 'E', 'F']
key_list = ['a', 'b', 'c', 'd', 'e', 'f']

def full_search() :
  for i in range(N) :
    for j in range(M) :
      if map_list[i][j] == '0' :
        print(bfs(j, i))
        return
        
def bfs(x, y) :
  q = deque([(x, y, 0, 0)])

  visited = [[[MAX]*M for _ in range(N)] for _ in range(1 << 6)]
  visited[0][y][x] = 0

  while q :
    x, y, dist, key_visited = q.popleft()
    if map_list[y][x] == '1' :
      return dist

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      next_key_visited = key_visited
      if -1 < ax < M and -1 < ay < N :
        if map_list[ay][ax] == '#' :
          continue
        if map_list[ay][ax] in door_list :
          door_idx = ord(map_list[ay][ax]) - ord('A')
          if not key_visited & (1 << door_idx) :
            continue
        if map_list[ay][ax] in key_list :
          key_idx = ord(map_list[ay][ax]) - ord('a')
          next_key_visited = key_visited | (1 << key_idx)

        if visited[next_key_visited][ay][ax] <= dist + 1 :
          continue
        visited[next_key_visited][ay][ax] = dist + 1
        q.append((ax, ay, dist+1, next_key_visited))

  return -1

full_search()


    