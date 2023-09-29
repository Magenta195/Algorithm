
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
well_cost = [int(input()) for _ in range(N)]
road_list = list()
for i in range(N) :
  road_cost = list(map(int, input().split()))
  for j in range(i+1, N) :
    road_list.append((road_cost[j], i, j))

road_list.sort()
parent = [(i, well_cost[i]) for i in range(N)]

def find(a) :
  if a == parent[a][0] :
    return parent[a]
  parent[a] = find(parent[a][0])
  return parent[a]

def union(a, b) :
  pa, pa_cost = find(a)
  pb, pb_cost = find(b)
  if pa_cost < pb_cost :
    parent[pb] = (pa, pa_cost)
  else :
    parent[pa] = (pb, pb_cost)

answer, cnt = 0, N-1
for cost, a, b in road_list :
  if not cnt :
    break
  pa, pa_cost = find(a)
  pb, pb_cost = find(b)
  if pa != pb and max(pa_cost, pb_cost) >= cost :
    cnt -= 1
    union(a, b)
    answer += cost

tree_set = set()
for i in range(N) :
  pi, pcost = find(i)
  if pi not in tree_set :
    tree_set.add(pi)
    answer += pcost
    
print(answer)