dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


n = int(input())
moves = input().strip()
min_x, max_x, min_y, max_y = 0, 0, 0, 0
x, y, k = 0, 0, 0
travel_set = set([(0, 0)])

for move in moves :
  if move == 'L' :
    k = (k - 1) % 4
  elif move == 'R' :
    k = (k + 1) % 4
  else :
    x += dx[k]
    y += dy[k]
    travel_set.add((x, y))
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)

map_list = [['#']*(max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
for x, y in travel_set :
  map_list[y - min_y][x - min_x] = '.'
for _map in map_list :
  print(''.join(_map))