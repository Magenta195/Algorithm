from heapq import *
import sys

input = sys.stdin.readline
MAX = float('inf')

def init() :
  N = int(input())
  coord_list = [list(map(int, input().split())) for _ in range(N+2)]

  graph_mat = { key : [] for key in range(N+2)}

  for i in range(N+1) :
    ix, iy = coord_list[i]
    for j in range(i+1, N+2) :
      jx, jy = coord_list[j]
      dist = abs(ix - jx) + abs(iy - jy)
      if dist <= 1000 :
        graph_mat[i].append(j)
        graph_mat[j].append(i)

  return N, graph_mat

def dijkstra(N, graph_mat) :
  visited = [MAX]*(N+2)
  visited[0] = 0
  q = [(0, 0)]

  while q :
    dist, node = heappop(q)
    if node == N+1 :
      return True

    next_dist = dist + 1
    for next_node in graph_mat[node] :
      if visited[next_node] > next_dist :
        visited[next_node] = next_dist 
        heappush(q, (next_dist, next_node))

  return False

def solve() :
  T = int(input())
  for i in range(T) :
    N, graph_mat = init()
    is_enable = dijkstra(N, graph_mat)
    print("happy" if is_enable else "sad")

solve()
