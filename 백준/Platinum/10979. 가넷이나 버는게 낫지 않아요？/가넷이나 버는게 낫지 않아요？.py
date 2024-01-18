from collections import defaultdict
from heapq import *
import sys
input = sys.stdin.readline
MAX = float('inf')

def dijkstra_youngsuk(edges, N) :
  dist = [(MAX, MAX, -1, -1)]*(N+1)
  dist[1] = (0, 0, 1, 0)
  q = [(0, 0, 1)]
  while q :
    t, g, n = heappop(q)
    if n == N :
      break
    for i, (_t, _g, x, _) in enumerate(edges[n]) :
      if dist[x] > (t + _t, g + _g, n, i) :
        dist[x] = (t + _t, g + _g, n, i)
        heappush(q, (t + _t, g + _g, x))
  n = N
  while n != dist[n][2] :
    n, i = dist[n][2], dist[n][3]
    edges[n][i][-1] = 1

def dijkstra_suckzoo(edges, N) :
  dist = [[(MAX, 0)]*2 for _ in range(N+1)]
  dist[1][1] = (0, 0)
  q = [(0, 0, 1, 1)]
  while q :
    t, g, matched, n = heappop(q)
    g = -g
    if n == N and not matched :
      return t, g
    for _t, _g, x, m in edges[n] :
      if dist[x][matched & m] > (t + _t, -g - _g) :
        dist[x][matched & m] = (t + _t, -g - _g)
        heappush(q, (t + _t, -g - _g, matched & m, x))

def solve(i) :
  N, M = map(int, input().split())
  edges = defaultdict(list)
  for _ in range(M) :
    x, y, t, g = map(int, input().split())
    edges[x].append([t, g, y, 0])
    edges[y].append([t, g, x, 0])

  dijkstra_youngsuk(edges, N)
  t, g = dijkstra_suckzoo(edges, N)
  print("Game #{}: Suckzoo ends game in time {}, earning {} garnet(s).".format(i+1, t, g))

T = int(input())
for i in range(T) :
  solve(i)