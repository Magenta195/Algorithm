from heapq import *
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cost = list(map(int, input().split()))
nxt_list = [[] for _ in range(N)]

for _ in range(M) :
  a, x, y = map(int, input().split())
  nxt_list[x-1].append((a-1, y-1))
  nxt_list[y-1].append((a-1, x-1))

q = []
for i in range(N) :
  heappush(q, (cost[i], i))

while q :
  c, n = heappop(q)
  for a, x in nxt_list[n] :
    if cost[a] > cost[x] + c :
      cost[a] = cost[x] + c
      heappush(q, (cost[a], a))

print(cost[0])