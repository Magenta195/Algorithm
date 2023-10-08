from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MAX = float('inf')

N, M = map(int, input().split())
edge_dict = defaultdict(list)
for _ in range(M) :
  a, b, c = map(int, input().split())
  edge_dict[a-1].append((b-1, c))
  edge_dict[b-1].append((a-1, c))

q = [(0, 0, 0)]
dist = [MAX]*N
prev_list = list(range(N))
while q :
  cost, prev, node = heappop(q)
  if dist[node] <= cost :
    continue
  dist[node] = cost
  prev_list[node] = prev
  for nxt, nxt_cost in edge_dict[node] :
    heappush(q, (cost + nxt_cost, node, nxt))

answer_set = set()
def backtrack(node) :
  if prev_list[node] == node :
    return
  if (prev_list[node]+1, node+1) in answer_set :
    return
  answer_set.add((prev_list[node]+1, node+1))
  backtrack(prev_list[node])

for i in range(N) :
  backtrack(i)

print(len(answer_set))
for answer in answer_set :
  print(*answer)