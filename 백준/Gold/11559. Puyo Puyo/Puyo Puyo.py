from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

map_list = [list(input().strip()) for _ in range(12)]

def check_chain() :
  global visited
  visited = [[False]*6 for _ in range(12)]
  tot_result = list()
  for i in range(12) :
    for j in range(6) :
      if map_list[i][j] == '.' :
        continue
      cnt, result = dfs(j, i)
      if cnt >= 4 :
        tot_result += result

  for x, y in tot_result :
    map_list[y][x] = '.'

  return len(tot_result) > 0 

def dfs(x, y) :
  typ = map_list[y][x]
  q = deque([(x, y)])
  visited[y][x] = True
  cnt = 0
  result = list()
  while q :
    x, y = q.pop()
    result.append((x, y))
    cnt += 1
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < 6 and -1 < ay < 12 and not visited[ay][ax] and map_list[ay][ax] == typ :
        visited[ay][ax] = True
        q.append((ax, ay))

  return cnt, result

def bubble_sort() :
  for k in range(6) :
    for i in range(11) :
      for j in range(i, 11) :
        if map_list[j+1][k] == '.' :
          map_list[j][k], map_list[j+1][k] = map_list[j+1][k], map_list[j][k]

answer = 0
enable = True
while enable :
  enable = check_chain()
  if enable :
    bubble_sort()
    answer += 1
print(answer)