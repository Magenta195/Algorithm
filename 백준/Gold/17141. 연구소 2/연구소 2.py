from itertools import combinations
from collections import deque

MAX = float('inf')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def init() :
  global N, M
  N, M = map(int, input().split())
  lab_mat = list()
  virus_list = list()
  
  for i in range(N) :
    _lab_mat = list(map(int, input().split()))
    for j in range(N) :
      if _lab_mat[j] == 2 :
        _lab_mat[j] = 0
        virus_list.append((j, i))
    lab_mat.append(_lab_mat)

  return lab_mat, virus_list

def check_full_spread(visited) :
  result = -1
  for _visited in visited :
    if MAX in _visited :
      return MAX
    result = max(result, max(_visited))
    
  return result

def virus_spread(lab_mat, comb) :
  visited = [[MAX if _lab_mat[i] == 0 else 0 for i in range(N)] for _lab_mat in lab_mat]

  q = deque()
  for x, y in comb :
    q.append((0, x, y))
    visited[y][x] = 0
  
  while q :
    dist, x, y = q.popleft()

    for k in range(4) :
      ax, ay = x+dx[k], y+dy[k]
      if -1 < ax < N and -1 < ay < N and lab_mat[ay][ax] == 0 and visited[ay][ax] > dist+1 :
        visited[ay][ax] = dist+1
        q.append((dist+1, ax, ay))

  result = check_full_spread(visited)
  return result

def full_spread(lab_mat, virus_list) :
  K = min(len(virus_list), M)
  result = MAX
  for comb in combinations(virus_list, K) :
    t = virus_spread(lab_mat, comb)
    result = min(result, t)

  return result if result < float('inf') else -1


def solve() :
  lab_mat, virus_list = init()
  result = full_spread(lab_mat, virus_list)
  print(result)

solve()