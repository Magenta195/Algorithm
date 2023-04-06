from heapq import *
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

MAX = float('inf')

def init() :
  global N, P, K, web_dict
  N, P, K = map(int, input().split())
  web_dict = defaultdict(list)
  for i in range(P) :
    a, b, cost = map(int, input().split())
    web_dict[a].append((b, cost))
    web_dict[b].append((a, cost))


def dijkstra(huddle) :
  q = [(0, 1, K)]
  cost_list = [[MAX]*(K+1) for _ in range(N+1)]
  cost_list[1][K] = 0

  while q :
    cost, node, skip_left = heappop(q)
    if node == N :
      continue

    for next_node, _cost in web_dict[node] :
      if _cost > huddle :
        next_skip_left = skip_left - 1
        next_cost = cost
      else :
        next_skip_left = skip_left
        next_cost = max(cost, _cost)

      if next_skip_left < 0 :
        continue

      if cost_list[next_node][next_skip_left] > next_cost :
        cost_list[next_node][next_skip_left] = next_cost
        heappush(q, (next_cost, next_node, next_skip_left))

  result = min(cost_list[N])
  return result

def binary_search() :
  start, end = 1, 1000000
  result = MAX
  while start <= end :
    mid = (start + end) // 2

    _result = dijkstra(mid)
    if _result < MAX :
      end = mid - 1
      result = min(result, _result)
    else :
      start = mid + 1

  return result

def solve() :
  init()
  result = binary_search()
  print(result if result < MAX else -1)

solve()