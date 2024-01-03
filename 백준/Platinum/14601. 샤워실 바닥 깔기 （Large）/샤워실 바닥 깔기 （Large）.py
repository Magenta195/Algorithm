
N = int(input())
maps = [[0]*(1 << N) for _ in range(1 << N)]
tx, ty = map(int, input().split())
tx -= 1
ty = (1 << N) - ty
cnt = 1
def leftover(x, y, dir, depth) :
  global cnt
  if depth == 1 :
    for i in range(2) :
      for j in range(2) :
        if i*2 + j == dir :
          continue
        maps[y+i][x+j] = cnt
    cnt += 1
    return
  length = 1 << (depth - 1)
  leftover(x + length // 2, y + length // 2, dir, depth-1)
  for i in range(2) :
    for j in range(2) :
      new_dir = (i*2 + j)
      if new_dir == dir :
        continue
      leftover(x + length * j, y + length * i, 3 - new_dir, depth - 1)
      
def div_and_con(x, y, depth) :
  if not depth :
    maps[y][x] = -1
    return
  length = 1 << (depth - 1)
  for i in range(2) :
    for j in range(2) :
      dir = i*2 + j
      ax = x + length * j
      ay = y + length * i
      if ax <= tx < ax + length and ay <= ty < ay + length :
        div_and_con(ax, ay, depth-1)
        leftover(x, y, dir, depth)
        return

div_and_con(0, 0, N)
for _maps in maps :
  print(*_maps)