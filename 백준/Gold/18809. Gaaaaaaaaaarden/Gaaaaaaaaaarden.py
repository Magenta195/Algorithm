from itertools import combinations
from collections import defaultdict
import sys

input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M, G, R = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
start_list = list()
for i in range(N) :
  for j in range(M) :
    if map_list[i][j] == 2 :
      start_list.append((j, i))

def bfs_ones(q, visited) :
  next_dict = defaultdict(set)
  next_q = list()
  cnt = 0
  for x, y, typ in q :
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N and map_list[ay][ax] and not visited[ay][ax] :
        next_dict[(ax, ay)].add(typ)
  for (x, y), val in next_dict.items() :
    visited[y][x] = True
    if len(val) > 1 :
      cnt += 1
      continue
    next_q.append((x, y, list(val)[0]))
  return next_q, cnt

def search(q, visited) :
  result = 0
  while q :
    q, cnt = bfs_ones(q, visited)
    result += cnt
  return result

answer = 0
for r_val in combinations(range(len(start_list)), R) :
  left_list = [ x for x in range(len(start_list)) if x not in r_val]
  for g_val in combinations(left_list, G) :
    q = list()
    visited = [[False]*M for _ in range(N)]
    for r in r_val :
      x, y = start_list[r]
      visited[y][x] = True
      q.append((x, y, 0))
    for g in g_val :
      x, y = start_list[g]
      visited[y][x] = True
      q.append((x, y, 1))
    result = search(q, visited)
    answer = max(answer, result)
print(answer)
