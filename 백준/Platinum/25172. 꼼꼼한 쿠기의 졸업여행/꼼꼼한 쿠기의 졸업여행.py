from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = list(range(N+1))
edge_dict = defaultdict(list)

for _ in range(M) : 
  a, b = map(int, input().split())
  edge_dict[a].append(b)
  edge_dict[b].append(a)

visited = [False] * (N+1)
graph = set()
connect_queue = [int(input()) for _ in range(N)]

def find(a) :
  if parents[a] == a :
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(a, b) :
  pa, pb = find(a), find(b)
  if pa > pb :
    pa, pb = pb, pa
  parents[pb] = pa
  return

def is_full_connected(n) :
  global graph
  visited[n] = True
  graph.add(n)
  for m in edge_dict[n] :
    if visited[m] :
      union(m, n)

  graph = { find(g) for g in graph }
  return len(graph) == 1

ans = ["DISCONNECT"]
for n in reversed(connect_queue) :
  res = "CONNECT" if is_full_connected(n) else "DISCONNECT"
  ans.append(res)

print(*reversed(ans), sep='\n')