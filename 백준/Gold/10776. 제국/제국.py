from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline
MAX = float('inf')

K, N, M = map(int, input().split())
dist = [[MAX]*(K+1) for _ in range(N+1)]
edge_dict = defaultdict(list)

for _ in range(M) :
  a, b, t, h = map(int, input().split())
  edge_dict[a].append((b, t, h))
  edge_dict[b].append((a, t, h))

S, E = map(int, input().split())
dist[S][K] = 0
q = [(0, K, S)]
flg = False
while q :
  d, k, n = heappop(q)
  if n == E :
    flg = True
    break
  for e, t, h in edge_dict[n] :
    if k - h <= 0 :
      continue
    if dist[e][k-h] > d + t :
      dist[e][k-h] = d + t
      heappush(q, (d+t, k-h, e))

print(d if flg else -1)