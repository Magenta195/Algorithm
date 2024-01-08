from bisect import bisect_left
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

def solve() :
  N = int(input())
  coord = []
  for _ in range(N) :
    x, y = map(int, input().split())
    coord.append([x, -y])
  coord, xlen, ylen = coord_compress(coord, N)
  tree = [0]*(xlen + 1)
  result = 0

  def update(i) :
    while i <= xlen :
      tree[i] += 1
      i += -i & i
  def search(i) :
    result = 0
    while i :
      result += tree[i]
      i -= -i & i
    return result

  for x, _ in reversed(coord) :
    update(x)
    sumval = search(xlen)
    xval = search(x-1) if x > 1 else 0
    result += sumval - xval - 1
  print(result)

for _ in range(int(input())) :
  solve()