import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
map_list = [list(map(str, input())) for _ in range(N)]

result = 0
for i in range(N) :
  for j in range(M) :
    if map_list[i][j] == 'L' :
      visited = [[False]*M for _ in range(N)]

      q = deque()
      q.append((j, i, 0))
      visited[i][j] = True

      while q :
        x, y, dist = q.popleft()
          
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1) ]:
          ax, ay = x + dx, y + dy
          if -1 < ax < M and -1 < ay < N and not visited[ay][ax] and map_list[ay][ax] == 'L' :
            visited[ay][ax] = True
            q.append((ax, ay, dist+1))

      if dist > result :
        result = dist

print(result)