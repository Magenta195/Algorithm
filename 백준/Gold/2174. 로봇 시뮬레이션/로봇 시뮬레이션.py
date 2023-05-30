

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dir = 'NWSE'

A, B = map(int, input().split())
N, M = map(int, input().split())
map_list = [[-1]*A for _ in range(B)]
robot_list = list()
for i in range(N) :
  x, y, d = input().split()
  x = int(x) - 1
  y = B - int(y)
  d = dir.index(d)
  map_list[y][x] = i
  robot_list.append([x, y, d])

def move(robot, num) :
  x, y, d = robot_list[robot]
  map_list[y][x] = -1
  for _ in range(num) :
    x, y = x + dx[d], y + dy[d]
    if not ( -1 < x < A and -1 < y < B ) :
      return 1, 0
    if map_list[y][x] > -1 :
      return 2, map_list[y][x]
  map_list[y][x] = robot
  robot_list[robot] = [x, y, d]
  return 0, 0

flg = True
for _ in range(M) :
  robot, order, num = input().split()
  robot, num = int(robot)-1, int(num)
  if order == 'L' :
    robot_list[robot][2] = (robot_list[robot][2] + num) % 4
  elif order == 'R' :
    robot_list[robot][2] = (robot_list[robot][2] - num) % 4
  else :
    result, crashed = move(robot, num)
    if result == 1 :
      print('Robot {} crashes into the wall'.format(robot+1))
      flg = False
      break
    if result == 2 :
      print('Robot {} crashes into robot {}'.format(robot+1, crashed+1))
      flg = False
      break
if flg :
  print('OK')