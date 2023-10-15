from collections import deque
import sys
input = sys.stdin.readline
MAX = float('inf')
N, K, M = map(int, input().split())

adj_nodes = [list() for _ in range(M+N)]

for i in range(N, N+M) :
  line = list(map(int, input().split()))
  for j in line :
    adj_nodes[j-1].append((i, 1))
    adj_nodes[i].append((j-1, 0))

visited = [MAX]*(N+M)
visited[0] = 0
q = deque([(0, 1)])

while q :
  node, dist = q.popleft()
  if node == N-1 :
    print(dist)
    exit()
  for adj, cost in adj_nodes[node] :
    if visited[adj] > dist + cost :
      visited[adj] = dist + cost
      q.append((adj, dist+cost))
print(-1)