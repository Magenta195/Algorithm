from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve() :
  K, M, P = map(int, input().split())
  edge_dict = defaultdict(list)
  indegree_list = [0]*M
  visited = [False]*M
  strahler_list = [[0]*2 for _ in range(M)]
  q = deque()
  
  for _ in range(P) :
    a, b = map(int, input().split())
    edge_dict[a-1].append(b-1)
    indegree_list[b-1] += 1

  for i in range(M) :
    if indegree_list[i] == 0 :
      q.append(i)
      visited[i] = True
      strahler_list[i] = [1, 1]

  while q :
    node = q.popleft()
    if strahler_list[node][1] > 1 :
      strahler_list[node][0] += 1
    
    for nxt in edge_dict[node] :
      indegree_list[nxt] -= 1
      if strahler_list[nxt][0] < strahler_list[node][0] :
        strahler_list[nxt] = [strahler_list[node][0], 1]
      elif strahler_list[nxt][0] == strahler_list[node][0] :
        strahler_list[nxt][1] += 1
      if not indegree_list[nxt] :
        q.append(nxt)
  print(K, strahler_list[-1][0])

T = int(input())
for _ in range(T) :
  solve()