import sys
input = sys.stdin.readline
MAX = float('inf')

def coord_compress(coord, N) :
  length = [0]*2
  prev = [-MAX]*2
  for i in range(2) :
    coord.sort(key = lambda x : (x[i], x[1-i]))
    for j in range(N) :
      if prev[i] < coord[j][i] :
        prev[i] = coord[j][i]
        length[i] += 1
      coord[j][i] = length[i]
      
  return coord, length[0]+1, length[1]+1

def update(i, xlen) :
  while i <= xlen :
    tree[i] += 1
    i += -i & i
def search(i) :
  result = 0
  while i :
    result += tree[i]
    i -= -i & i
  return result

def solve() :
  global tree
  N = int(input())
  coord = [list(map(int, input().split())) for _ in range(N)]
  coord, xlen, ylen = coord_compress(coord, N)
  coord.sort(key = lambda x : (x[1], -x[0]))
  tree = [0]*(xlen + 1)
  result = 0
  for x, _ in coord :
    result += search(xlen-x)
    update(xlen-x, xlen)
  print(result)

for _ in range(int(input())) :
  solve()