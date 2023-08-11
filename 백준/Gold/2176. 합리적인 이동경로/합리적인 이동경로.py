from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MAX = float('inf')
N, M = map(int, input().split())
edge_list = defaultdict(list)
for _ in range(M) :
  a, b, dist = map(int, input().split())
  edge_list[a-1].append((b-1, dist))
  edge_list[b-1].append((a-1, dist))

dp = [-1]*N
dist_list = [MAX]*N
dist_list[1] = 0
q = [ (0, 1) ]

def dfs(node) :
  if node == 1 :
    return 1
  if dp[node] > -1 :
    return dp[node]

  result = 0
  for nxt, _ in edge_list[node] :
    if dist_list[node] > dist_list[nxt] :
      result += dfs(nxt)
  dp[node] = result
  return dp[node]

while q :
  dist, node = heappop(q)

  if dist_list[node] < dist :
    continue

  for nxt, nxt_dist in edge_list[node] :
    if dist_list[nxt] > dist + nxt_dist :
      dist_list[nxt] = dist + nxt_dist
      heappush(q, (dist + nxt_dist, nxt))

if dist_list[0] == MAX :
  print(0)
else :
  print(dfs(0))