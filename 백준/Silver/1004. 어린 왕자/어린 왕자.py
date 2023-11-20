import sys
input = sys.stdin.readline

def isin(x, y, tx, ty, r) :
  return (x - tx) ** 2 + (y - ty) ** 2 <= r ** 2

def solve() :
  sx, sy, ex, ey = map(int, input().split())
  cnt = 0
  for _ in range(int(input())) :
    x, y, r = map(int, input().split())
    sin = isin(x, y, sx, sy, r)
    ein = isin(x, y, ex, ey, r)

    if sin^ein :
      cnt += 1
  print(cnt)

for _ in range(int(input())) :
  solve()