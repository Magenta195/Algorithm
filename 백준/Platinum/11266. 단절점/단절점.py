import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
MAX = float('inf')

V, E = map(int, input().split())

visit_order = [MAX]*V
order = 0
answer = set()
edge_dict = defaultdict(list)
for _ in range(E) :
  a, b = map(int, input().split())
  edge_dict[a-1].append(b-1)
  edge_dict[b-1].append(a-1)

def dfs(node, isroot) :
  global order
  visit_order[node] = order
  order += 1
  child_num = 0
  child_order = visit_order[node]
  
  for nxt in edge_dict[node] :
    if visit_order[nxt] < MAX :
      child_order = min(child_order, visit_order[nxt])
    else :
      child_num += 1
      tmp = dfs(nxt, False)
      if not isroot and tmp >= visit_order[node] :
        answer.add(node+1)
      child_order = min(child_order, tmp)
      
  if isroot and child_num >= 2 :
    answer.add(node+1)
  return child_order

for i in range(V) :
  if visit_order[i] == MAX :
    dfs(i, True)
answer = sorted(list(answer))
print(len(answer))
print(*answer)