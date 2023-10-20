from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
prepared = [0]*N
cost = [0]*N
next_tiers = defaultdict(list)

for i in range(N) :
  lst = list(map(int, input().split()))
  cost[i] = lst[0]
  for j in lst[1:] :
    if j == -1 :
      break
    next_tiers[j-1].append(i)
    prepared[i] += 1

q = list()
for i in range(N) :
  if prepared[i] == 0 :
    heappush(q, (cost[i], i))

ans = [float('inf')]*N
while q :
  c, build = heappop(q)
  ans[build] = min(ans[build], c)
  for nxt in next_tiers[build] :
    prepared[nxt] -= 1
    if prepared[nxt] == 0 :
      heappush(q, (c + cost[nxt], nxt))

print(*ans, sep='\n')