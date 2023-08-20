import sys
input = sys.stdin.readline
N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]

def div(x, y, length) :
  if length == 1 :
    return (1, 0) if map_list[y][x] == 0 else (0, 1)

  r0, r1 = 0, 0
  for _y in [y, y + length // 2] :
    for _x in [x, x + length // 2] :
      t0, t1 = div(_x, _y, length // 2)
      r0 += t0
      r1 += t1

  if (r0, r1) == (0, 4) :
    return (0, 1)
  if (r0, r1) == (4, 0) :
    return (1, 0)
  return (r0, r1)

for result in div(0, 0, N) :
  print(result)