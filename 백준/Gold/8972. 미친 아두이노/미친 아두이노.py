from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = float('inf')
dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

R, C = map(int, input().split())
map_list = [list(input().strip()) for _ in range(R)]

arduino_list = set()
tr, tc = -1, -1

for r in range(R) :
  for c in range(C) :
    if map_list[r][c] == 'I' :
      tr, tc = r, c
    elif map_list[r][c] == 'R' :
      arduino_list.add((r, c))

move_set = input().strip()

flg = True
for idx, move in enumerate(move_set) :
  move = int(move) - 1
  tr, tc = tr + dr[move], tc + dc[move]
  next_arduino_list = set()
  crashed = set()
  for r, c in arduino_list :
    br, bc, bdist = -1, -1, MAX
    for k in range(9) :
      _br, _bc = r + dr[k], c + dc[k]
      if abs(_br - tr) + abs(_bc - tc) < bdist :
        br, bc, bdist = _br, _bc, abs(_br - tr) + abs(_bc - tc)
    if tr == br and tc == bc :
      flg = False
      break
    if (br, bc) in next_arduino_list :
      crashed.add((br, bc))
    else :
      next_arduino_list.add((br, bc))
  
  if not flg :
    break
  arduino_list = next_arduino_list - crashed

if not flg :
  print("kraj {}".format(idx+1))
else :
  result = [['.']*C for _ in range(R)]
  result[tr][tc] = 'I'
  for r, c in arduino_list :
    result[r][c] = 'R'
  for _result in result :
    print(''.join(_result))