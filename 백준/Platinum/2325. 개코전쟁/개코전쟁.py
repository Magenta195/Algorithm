from collections import defaultdict
from heapq import *
import sys

input = sys.stdin.readline
MAX = float('inf')

N, M = map(int, input().split())
edge_dict = defaultdict(list)

for _ in range(M):
  a, b, c = map(int, input().split())
  edge_dict[a].append((b, c))
  edge_dict[b].append((a, c))
s, e = 1, N

def dijkstra(start, end, forbid=None):
  q = [(0, start)]
  dist = [(MAX, MAX)]*(N + 1)
  dist[start] = (0, start)
  while q:
    d, n = heappop(q)
    if dist[n][0] < d:
      continue
    if n == end:
      return dist, d
    for nxt, c in edge_dict[n]:
      if (n, nxt) == forbid or (nxt, n) == forbid:
        continue
      if dist[nxt][0] > d + c:
        dist[nxt] = (d + c, n)
        heappush(q, (d + c, nxt))

backtrack, _ = dijkstra(s, e)
ans = 0
node = e
while node != s:
  prev = backtrack[node][1]
  _, d = dijkstra(s, e, (prev, node))
  ans = max(ans, d)
  node = prev
print(ans)