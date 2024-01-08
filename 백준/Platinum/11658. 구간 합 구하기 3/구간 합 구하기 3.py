import sys
input = sys.stdin.readline
MAX = float('inf')

N, M = map(int, input().split())
tree = [[0]*(N+1) for _ in range(N+1)]

def update(x, y, val) :
  while x <= N :
    tree[y][x] += val
    x += -x & x
    
def update2D(x, y, val) :
  while y <= N :
    update(x, y, val)
    y += -y & y

def search(x, y) :
  result = 0
  while x :
    result += tree[y][x]
    x -= -x & x
  return result

def search2D(x, y) :
  if not x or not y :
    return 0
  result = 0
  while y :
    result += search(x, y)
    y -= -y & y
  return result

maps = [list(map(int, input().split())) for _ in range(N)]
for i in range(N) :
  for j in range(N) :
    update2D(j+1, i+1, maps[i][j])

for _ in range(M) :
  w, *cmd = map(int, input().split())
  if w == 0 :
    y, x, c = cmd
    update2D(x, y, c - maps[y-1][x-1])
    maps[y-1][x-1] = c
  else :
    y1, x1, y2, x2 = cmd
    print(search2D(x2, y2)+search2D(x1-1, y1-1)-search2D(x2, y1-1)-search2D(x1-1, y2))