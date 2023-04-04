N = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

map_list = [input().split() for _ in range(N)]

def search() :
  result = list()
  for i in range(N) :
    for j in range(N) :
      if map_list[i][j] == 'T' :
        for k in range(4) :
          x, y = j + dx[k], i + dy[k]
          if -1 < x < N and -1 < y < N :
            flg, teacher_eyesight = check_lines(x, y, k)
            if not flg and not teacher_eyesight :
              return False, list()
            if flg :
              result.append(teacher_eyesight)

  return True, result
          

def check_lines(x, y, r) :
  if map_list[y][x] == 'S' :
    return False, set()
    
  result = set()
  flg = False
  while -1 < x < N and -1 < y < N :
    if map_list[y][x] == 'S' :
      flg = True
      break
    result.add((x, y))
    x, y = x + dx[r], y + dy[r]

  return flg, result

def check_eyesight(teacher_list) :
  length = len(teacher_list)
  visited = [False]*length
  cnt = 0
  
  for i in range(length) :
    if visited[i] :
      continue
    cnt += 1
    visited[i] = True
    for j in range(i+1, length) :
      if teacher_list[i].intersection(teacher_list[j]) :
        visited[j] = True

  return cnt <= 3

def solve() :
  is_enable, teacher_list = search()
  if not is_enable :
    print('NO')
    return
  is_avoidable = check_eyesight(teacher_list)
  print('YES' if is_avoidable else 'NO')

solve()
  