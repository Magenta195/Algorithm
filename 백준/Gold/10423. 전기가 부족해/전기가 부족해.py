from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
power_plants = list(map(int, input().split()))
cable_dict = defaultdict(list)

for _ in range(M) :
  u, v, w = map(int,input().split())
  cable_dict[u-1].append((v-1, w))
  cable_dict[v-1].append((u-1, w))

answer = 0
q = []
visited = [False]*N
left = N - K
for idx in power_plants :
  visited[idx-1] = True
  for node, cost in cable_dict[idx-1] :
    heappush(q, (cost, node))

while q and left :
  cost, node = heappop(q)
  if visited[node] :
    continue
  answer += cost
  visited[node] = True
  left -= 1
  for nxt, cost in cable_dict[node] :
    if not visited[nxt] :
      heappush(q, (cost, nxt))

print(answer)