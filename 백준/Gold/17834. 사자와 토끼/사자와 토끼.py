from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_dict = defaultdict(list)
for _ in range(M) :
  a, b = map(int, input().split())
  edge_dict[a].append(b)
  edge_dict[b].append(a)

color = [-1]*(N+1)
q = [(1, 0)]
color[1] = 0
flg = True
while q :
  n, c = q.pop()
  for nxt in edge_dict[n] :
    if color[nxt] == c :
      flg = False
      break
    if color[nxt] == -1 :
      color[nxt] = 1-c
      q.append((nxt, 1-c))

if not flg :
  print(0)
else :
  print(color.count(0) * color.count(1) * 2)