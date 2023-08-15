
from collections import deque
import sys
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
MAX = float('inf')
R, C = map(int, input().split())
map_list = [input().strip() for _ in range(R)]
visited = [[MAX]*C for _ in range(R)]
fq = deque()
jq = deque()

def init() :
  for r in range(R) :
    for c in range(C) :
      if map_list[r][c] == 'F' :
        fq.append((r, c, 0))
        visited[r][c] = 0
      elif map_list[r][c] == 'J' :
        jq.append((r, c, 0))

def bfs(q, mode = False) :    
  while q :
    r, c, d = q.popleft()
    for k in range(4) :
      ar, ac = r + dr[k], c + dc[k]
      if -1 < ar < R and -1 < ac < C :
        if map_list[ar][ac] != '#' and visited[ar][ac] > d + 1 :
          visited[ar][ac] = d + 1
          q.append((ar, ac, d+1))
      elif mode :
        return d + 1
  return MAX

init()
_ = bfs(fq)
result = bfs(jq, mode = True)

print(result if result < MAX else 'IMPOSSIBLE')