from collections import deque
import sys

input = sys.stdin.readline
cvt = lambda x : int(x) - 1

while True :
  n = int(input())
  if not n :
    break
  maze_list = list()
  for _ in range(n) :
    typ, money, *next_list = input().split()
    next_list = list(map(cvt, next_list[:-1]))
    maze_list.append([typ, int(money), next_list])

  visited = [-1]*n  
  flg = False

  if maze_list[0][0] == 'T' and maze_list[0][1] > 0 :
    print('No')
    continue
  elif maze_list[0][0] == 'L' :
    q = deque([(0, maze_list[0][1])])
    visited[0] = maze_list[0][1]
  else :
    q = deque([(0, 0)])
    visited[0] = 0
  
  while q :
    cur, money = q.popleft()
    if cur == n-1 :
      flg = True
      break
    for node in maze_list[cur][2] :
      if maze_list[node][0] == 'T' :
        if maze_list[node][1] > money :
          continue
        next_money = money - maze_list[node][1]
      elif maze_list[node][0] == 'L' :
        next_money = max(money, maze_list[node][1])
      else :
        next_money = money
      if visited[node] < next_money :
        visited[node] = next_money
        q.append((node, next_money))

  print('Yes' if flg else 'No')
  
