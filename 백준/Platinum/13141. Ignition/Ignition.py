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

for k in range(1, N+1) :
  for i in range(1, N) :
    for j in range(i+1, N+1) :
      if i == k or j == k :
        continue
      if min_edge[i][j] > min_edge[i][k] + min_edge[k][j] :
        min_edge[i][j] = min_edge[j][i] = min_edge[i][k] + min_edge[k][j]

for k in range(1, N+1) :
  min_edge[k][k] = 0
  result = 0.
  for i in range(1, N+1) :
    for j in range(i, N+1) :
      if not max_edge[i][j] :
        continue
      result = max(result, min_edge[k][i], min_edge[k][j])
      if abs(min_edge[k][i] - min_edge[k][j]) != max_edge[i][j] :
        result = max(result, max(min_edge[k][i], min_edge[k][j]) + (max_edge[i][j] - abs(min_edge[k][i] - min_edge[k][j])) / 2)
  ans = min(ans, result)

print('{:.01f}'.format(ans))