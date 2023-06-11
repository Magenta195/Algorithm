from collections import deque
import sys
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
MAX = float('inf')

input = sys.stdin.readline
N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
q = deque()

visited = [[MAX]*M for _ in range(N)]
for i in range(N) :
  for j in range(M) :
    if map_list[i][j] == 1 :
      q.append((j, i, 0))
      visited[i][j] = 0

while q :
  x, y, dist = q.popleft()
  for k in range(8) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < M and -1 < ay < N and visited[ay][ax] > dist + 1:
      visited[ay][ax] = dist + 1
      q.append((ax, ay, dist + 1))

print(max(map(max, visited)))