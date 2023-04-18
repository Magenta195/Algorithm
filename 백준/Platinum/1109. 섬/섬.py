
from collections import Counter
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def init() :
  global N, M, map_list
  N, M = map(int, input().split())
  map_list = [input().strip() for _ in range(N)]

def full_dfs(x, y, idx, visited) :
  q = [(x, y)]
  visited[y][x] = idx
  
  while q :
    x, y = q.pop()

    for k in range(8) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N and map_list[ay][ax] == 'x' and visited[ay][ax] == -1 :
        visited[ay][ax] = idx
        q.append((ax, ay))

def inside_dfs(x, y, idx, visited) :
  is_outside = False
  contact_set = set()
  q = [(x, y)]

  while q :
    x, y = q.pop()

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N :
        if visited[ay][ax] == -1 :
          visited[ay][ax] = idx
          q.append((ax, ay))
        elif visited[ay][ax] != idx :
          contact_set.add(visited[ay][ax])
      else :
        is_outside = True

  return is_outside, contact_set

def full_search() :
  global visited, target_node
  visited = [[-1]*M for _ in range(N)]
  target_node = list()
  idx = 0
  
  for i in range(N) :
    for j in range(M) :
      if map_list[i][j] == 'x' and visited[i][j] == -1 :
        full_dfs(j, i, idx, visited)
        target_node.append((j, i))
        idx += 1

def bfs(node, contact_dict, score_list, visited) :
  nxt_list = list()
  for nxt in contact_dict[node] :
    if not visited[nxt] :
      visited[nxt] = True
      nxt_list.append(nxt)

  result = 0
  for nxt in nxt_list :
    result = max(result, bfs(nxt, contact_dict, score_list, visited) + 1 )

  score_list[node] = result
  return result
  
  

def inside_search() :
  score_list = list()
  outside_list = list()
  contact_dict = dict()
  for idx, (x, y) in enumerate(target_node) :
    local_visited = [_visited[:] for _visited in visited]
    is_outside, contact_set = inside_dfs(x, y, idx, local_visited)
    
    if is_outside :
      outside_list.append(idx)
      
    contact_dict[idx] = contact_set

  for i in range(idx+1) :
    for j in contact_dict[i] :
      contact_dict[j].add(i)

  
  inside_visited = [ x in outside_list for x in range(idx+1)]
  score_list = [0]*(idx+1)

  
  for node in outside_list :
    bfs(node, contact_dict, score_list, inside_visited)
    
  maxval = max(score_list)
  counter = Counter(score_list)
  fscore_list = [0]*(maxval+1)
  for key, val in counter.items() :
    fscore_list[key] = val

  print(*fscore_list)

def solve() :
  init()
  full_search()
  if not target_node :
    print(-1)
    return
  inside_search()

solve()
      

  