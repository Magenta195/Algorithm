from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
MAX = N*M+1
maps = [input().strip() for _ in range(N)]
pq, sq = deque(), deque()

p_visited = [[MAX]*M for _ in range(N)]
isdead = [[MAX]*M for _ in range(N)]
y_min = [[MAX]*M for _ in range(N)]
x_min = [[MAX]*M for _ in range(N)]

def init() :
  global treasure
  for i in range(N) :
    for j in range(M) :
      if maps[i][j] == 'T' :
        treasure = (j, i)
      if maps[i][j] == 'Y' :
        sq.append((j, i, 0))
      if maps[i][j] == 'V' :
        pq.append((j, i, 1))
        p_visited[i][j] = 1

def shoot() :
  for i in range(N) :
    prev, minval = 0, p_visited[i][0]
    for j in range(1, M) :
      if maps[i][j] == 'I' :
        for k in range(prev, j) :
          isdead[i][k] = min(isdead[i][k], minval)
        prev, minval = j, p_visited[i][j]
      else :
        minval = min(minval, p_visited[i][j])
    for k in range(prev, M) :
      isdead[i][k] = min(isdead[i][k], minval)
    
  for i in range(M) :
    prev, minval = 0, p_visited[0][i]
    for j in range(1, N) :
      if maps[j][i] == 'I' :
        for k in range(prev, j) :
          isdead[k][i] = min(isdead[k][i], minval)
        prev, minval = j, p_visited[j][i]
      else :
        minval = min(minval, p_visited[j][i])
    for k in range(prev, N) :
      isdead[k][i] = min(isdead[k][i], minval)
      
def p_bfs() :
  while pq :
    x, y, cnt = pq.popleft()
    for i in range(4) :
      ax, ay = x + dx[i], y + dy[i]
      if -1 < ax < M and -1 < ay < N and maps[ay][ax] != 'I' and p_visited[ay][ax] > cnt :
        p_visited[ay][ax] = cnt
        pq.append((ax, ay, cnt+1))
  shoot()

def s_bfs() :
  while sq :
    x, y, cnt = sq.popleft()
    if (x, y) == treasure :
      return True
    for i in range(4) :
      ax, ay = x + dx[i], y + dy[i]
      if -1 < ax < M and -1 < ay < N and maps[ay][ax] != 'I' and isdead[ay][ax] > cnt+1 :
        isdead[ay][ax] = cnt+1
        sq.append((ax, ay, cnt+1))
  return False

init()
p_bfs()
print("YES" if s_bfs() else "NO")