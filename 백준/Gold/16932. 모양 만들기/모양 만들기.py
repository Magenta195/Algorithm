from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
adjList = [[set() for _ in range(M)] for _ in range(N)]
shapeList = []


def bfs(x, y, index) :
  count = 1
  queue = deque([(x, y)])
  visited[y][x] = True
  
  while queue :
    x, y = queue.popleft()
    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ay < N and -1 < ax < M :
        if maps[ay][ax] == 1 and not visited[ay][ax] :
          visited[ay][ax] = True
          queue.append((ax, ay))
          count += 1
        if maps[ay][ax] == 0 :
          adjList[ay][ax].add(index)
  shapeList.append(count)

index = 0
for i in range(N) :
  for j in range(M) :
    if not visited[i][j] and maps[i][j] == 1 :
      bfs(j, i, index)
      index += 1

answer = 0
for i in range(N) :
  for j in range(M) :
    if maps[i][j] == 0 :
      tmp = 1
      for k in adjList[i][j] :
        tmp += shapeList[k]
      answer = max(answer, tmp)

print(answer)