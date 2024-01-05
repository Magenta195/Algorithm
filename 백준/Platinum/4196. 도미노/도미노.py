from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
MAX = float('inf')

def solve() :
  global idx, scc_idx
  N, M = map(int, input().split())

  scc_visited = [MAX]*(N+1)
  scc_node = [-1]*(N+1)
  stk = list()
  scc_idx = 0
  idx = 0
  result = 0

  edge_dict = defaultdict(list)
  for _ in range(M) :
    a, b = map(int, input().split())
    edge_dict[a].append(b)
    
  def scc(node) :
    global idx, scc_idx
    ret = scc_visited[node] = idx
    idx += 1
    stk.append(node)
    
    for nxt in edge_dict[node] :
      if scc_node[nxt] > -1 :
        continue
      if scc_visited[nxt] == MAX :
        scc(nxt)
      scc_visited[node] = min(scc_visited[node], scc_visited[nxt])

    if scc_visited[node] == ret :
      while stk :
        n = stk.pop()
        scc_node[n] = scc_idx
        if n == node :
          break
      scc_idx += 1

  for i in range(1, N+1) :
    if scc_visited[i] == MAX :
      scc(i)

  order = [0]*scc_idx
  for i in range(1, N+1) :
    for j in edge_dict[i] :
      if scc_node[i] == scc_node[j] :
        continue
      order[scc_node[j]] += 1

  for i in range(scc_idx) :
    if not order[i] :
      result += 1
  print(result)

for _ in range(int(input())) :
  solve()