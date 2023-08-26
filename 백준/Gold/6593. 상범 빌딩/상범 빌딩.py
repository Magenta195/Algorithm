from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def solve() :
  Z, Y, X = map(int, input().split())
  if Z == Y == X == 0:
    return False
  map_list = list()
  for z in range(Z) :
    _map_list = list()
    for y in range(Y) :
      __map_list = input().strip()
      for x in range(X) :
        if __map_list[x] == 'E' :
          ex, ey, ez = x, y, z
        if __map_list[x] == 'S' :
          sx, sy, sz = x, y, z
      _map_list.append(__map_list)
    map_list.append(_map_list)
    input()

  visited = [[[False]*X for _ in range(Y)] for _ in range(Z)]
  visited[sz][sy][sx] = True
  q = deque([(sx, sy, sz, 0)])
  while q :
    x, y, z, t = q.popleft()
    if x == ex and y == ey and z == ez :
      print("Escaped in {} minute(s).".format(t))
      return True
    for k in range(6) :
      ax, ay, az = x + dx[k], y + dy[k], z + dz[k]
      if -1 < ax < X and -1 < ay < Y and -1 < az < Z and map_list[az][ay][ax] != '#' and not visited[az][ay][ax] :
        visited[az][ay][ax] = True
        q.append((ax, ay, az, t+1))
  print("Trapped!")
  return True

flg = True
while flg :
  flg = solve()