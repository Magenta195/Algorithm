from itertools import permutations, product
from collections import deque

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]
MAX = float('inf')

map_list = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
map_dict = { key : list() for key in range(5) }

for n in range(5) :
  maps = map_list[n]
  for _ in range(4) :
    result = [[0]*5 for _ in range(5)]
    for i in range(5) :
      for j in range(5) :
        result[i][j] = maps[4-j][i]
    map_dict[n].append(result)
    maps = result

def bfs(maps) :
  if maps[0][0][0] == 0 or maps[-1][-1][-1] == 0 :
    return MAX
  q = deque([(0, 0, 0, 0)])
  visited = [[[MAX]*5 for _ in range(5)] for _ in range(5)]
  visited[0][0][0] = 0
  while q :
    x, y, z, dist = q.popleft()
    if x == y == z == 4 :
      return dist
    for k in range(6) :
      ax, ay, az = x + dx[k], y + dy[k], z + dz[k]
      if -1 < ax < 5 and -1 < ay < 5 and -1 < az < 5 and maps[az][ay][ax] == 1 and visited[az][ay][ax] > dist + 1 :
        visited[az][ay][ax] = dist+1
        q.append((ax, ay, az, dist+1))

  return MAX

result = MAX
for perm in permutations(range(5)) :
  for pro in product(range(4), repeat = 5) :
    _map_list = [ map_dict[i][j] for i, j in zip(perm, pro) ]
    tmp = bfs(_map_list)
    if tmp == 12 :
      print(12) # min value
      exit()
    if tmp < result :
      result = tmp
print(result if result < MAX else -1)