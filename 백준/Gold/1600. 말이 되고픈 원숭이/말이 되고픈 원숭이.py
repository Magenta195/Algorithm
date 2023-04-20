from collections import deque
import sys
input = sys.stdin.readline
MAX = float('inf')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dkx = [-2, -2, -1, -1, 1, 1, 2, 2]
dky = [-1, 1, -2, 2, -2, 2, -1, 1]

def init() :
  global K, H, W, map_list
  K = int(input())
  W, H = map(int, input().split())
  map_list = [list(map(int, input().split())) for _ in range(H)]

def bfs() :
  visited = [[[MAX]*(K+1) for _ in range(W)] for _ in range(H)]

  visited[0][0][K] = 0

  q = deque([(0, 0, 0, K)])

  while q :
    x, y, dist, left = q.popleft()

    if x == W-1 and y == H-1 :
      print(dist)
      return

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < W and -1 < ay < H and map_list[ay][ax] == 0 and visited[ay][ax][left] > dist + 1 :
        visited[ay][ax][left] = dist + 1
        q.append((ax, ay, dist+1, left))

    if not left :
      continue

    for k in range(8) :
      ax, ay = x + dkx[k], y + dky[k]
      if -1 < ax < W and -1 < ay < H and map_list[ay][ax] == 0 and visited[ay][ax][left-1] > dist + 1 :
        visited[ay][ax][left-1] = dist + 1
        q.append((ax, ay, dist+1, left-1))
          
  print(-1)

def solve() :
  init()
  bfs()

solve()