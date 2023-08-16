from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = float('inf')
dr = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

R, C = map(int, input().split())
map_list = [list(input().strip()) for _ in range(R)]

arduino_list = list()
tr, tc = -1, -1
arduino_visited = defaultdict(int)

for r in range(R) :
  for c in range(C) :
    if map_list[r][c] == 'I' :
      tr, tc = r, c
    elif map_list[r][c] == 'R' :
      arduino_list.append((r, c))
      arduino_visited[(r, c)] += 1

move_set = input().strip()

flg = True
for idx, move in enumerate(move_set) :
  move = int(move) - 1
  tr, tc = tr + dr[move], tc + dc[move]
  for r, c in arduino_list :
    arduino_visited[(r, c)] -= 1
    br, bc, bdist = -1, -1, MAX
    for k in range(9) :
      _br, _bc = r + dr[k], c + dc[k]
      if abs(_br - tr) + abs(_bc - tc) < bdist :
        br, bc, bdist = _br, _bc, abs(_br - tr) + abs(_bc - tc)
    if tr == br and tc == bc :
      flg = False
      break
    arduino_visited[(br, bc)] += 1

  if not flg :
    break
  next_arduino_list = list()
  for key in arduino_visited :
    if arduino_visited[key] > 0 :
      if arduino_visited[key] == 1 :
        next_arduino_list.append(key)
      else :
        arduino_visited[key] = 0
  arduino_list = next_arduino_list

if not flg :
  print("kraj {}".format(idx+1))
else :
  result = [['.']*C for _ in range(R)]
  result[tr][tc] = 'I'
  for r, c in arduino_list :
    result[r][c] = 'R'
  for _result in result :
    print(''.join(_result))