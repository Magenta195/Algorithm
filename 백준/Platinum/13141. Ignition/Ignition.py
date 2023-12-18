from collections import deque
import sys
input = sys.stdin.readline
MAX = float('inf')

N, M = map(int, input().split())
min_edge = [[MAX]*(N+1) for _ in range(N+1)]
max_edge = [[0]*(N+1) for _ in range(N+1)]
ans = MAX
for _ in range(M) :
  S, E, L = map(int, input().split())
  min_edge[E][S] = min_edge[S][E] = min(min_edge[S][E], L)
  max_edge[E][S] = max_edge[S][E] = max(max_edge[S][E], L)

def bfs(init) :
  global ans
  visited = [float('inf')]*(N+1)
  visited[init] = 0
  q = deque([(init, 0)])
  
  while q :
    node, t = q.popleft()

    for i in range(1, N+1) :
      if min_edge[node][i] == MAX:
        continue
      if visited[i] > t + min_edge[node][i] :
        visited[i] = t + min_edge[node][i]
        q.append((i, t + min_edge[node][i]))

  result = 0.
  for i in range(1, N+1) :
    for j in range(1, N+1) :
      if not max_edge[i][j] :
        continue
      result = max(result, visited[i], visited[j])
      if abs(visited[i] - visited[j]) != max_edge[i][j] :
        result = max(result, max(visited[i], visited[j]) + (max_edge[i][j] - abs(visited[i] - visited[j])) / 2)
  ans = min(ans, result)

for i in range(1, N+1) :
  bfs(i)
print('{:.01f}'.format(ans))