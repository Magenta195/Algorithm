import sys
input = sys.stdin.readline
N = int(input())
map_list = [input().strip() for _ in range(N)]

flg = True
for i in range(N) :
  for j in range(N) :
    if map_list[i][j] == '*' :
      flg = False
      x, y = j, i+1
      print(y+1, x+1)
      break
  if not flg :
    break

answer = list()
l, lx, ly = 0, x, y
while -1 < lx and map_list[ly][lx] == '*':
  l += 1
  lx -= 1
answer.append(l-1)
r, rx, ry = 0, x, y
while rx < N and map_list[ry][rx]  == '*' :
  r += 1
  rx += 1
answer.append(r-1)
w = 0
while y < N and map_list[y][x] == '*' :
  w += 1
  y += 1
answer.append(w-1)
y -= 1
ll, llx, lly = 1, x-1, y+1
while lly < N and map_list[lly][llx] == '*' :
  ll += 1
  lly += 1
answer.append(ll - 1)
rl, rlx, rly = 1, x+1, y+1
while rly < N and map_list[rly][rlx] == '*' :
  rl += 1
  rly += 1
answer.append(rl - 1)
print(*answer)
