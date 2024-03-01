from heapq import *
from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = float('inf')

N, M, K, L, P = map(int, input().split())
switch = set(map(int, input().split()))
edge_dict = defaultdict(list)
trap_edge_dict = [ defaultdict(list) for _ in range(2) ]

for i in range(M) :
  a, b, c = map(int, input().split())
  if i >= M-L :
    trap_edge_dict[0][a].append((b, c))
    trap_edge_dict[1][b].append((a, c))
  else :
    edge_dict[a].append((b, c))
S, E = map(int, input().split())

dist = [[MAX]*(N+1) for _ in range(P*2)]
q = [(0, S, 0)]
dist[0][S] = 0
flg = False

while q :
  d, node, tag = heappop(q)
  if node == E :
    flg = True
    break
  for nxt, cost in edge_dict[node] :
    nxt_tag = (tag + 1) % (P*2) if nxt in switch else tag
    if dist[nxt_tag][nxt] > d + cost :
      dist[nxt_tag][nxt] = d + cost
      heappush(q, (d + cost, nxt, nxt_tag))

  for nxt, cost in trap_edge_dict[tag // P][node] :
    nxt_tag = (tag + 1) % (P*2) if nxt in switch else tag
    if dist[nxt_tag][nxt] > d + cost :
      dist[nxt_tag][nxt] = d + cost
      heappush(q, (d + cost, nxt, nxt_tag))

print(d if flg else -1)
    