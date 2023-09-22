from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline
MAX = float('inf')

K = int(input())
N = int(input())
R = int(input())

edge_dict = defaultdict(list)
for _ in range(R) :
  s, d, l, t = map(int, input().split())
  edge_dict[s-1].append((d-1, l, t))

dp = [[MAX]*(K+1) for _ in range(N)]
dp[0][K] = 0
q = [(0, K, 0)]
answer = MAX

while q :
  dist, cost, node = heappop(q)
  if node == N-1 :
    answer = min(answer, dist)
    break

  for nxt, nxt_dist, nxt_cost in edge_dict[node] :
    if cost - nxt_cost > -1 and dp[nxt][cost - nxt_cost] > dist + nxt_dist :
      dp[nxt][cost - nxt_cost] = dist + nxt_dist
      heappush(q, (dist + nxt_dist, cost - nxt_cost, nxt ))

print(answer if answer < MAX else -1)