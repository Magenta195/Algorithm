from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, P = map(int, input().split())
p_list = list(map(int, input().split()))
map_list = [list(input().strip()) for _ in range(N)]
result = [0] * P

def bfs(next_list, num) :
  q = deque()
  for x, y in next_list[idx] :
    q.append((x, y, 0))

  next_list[idx].clear()
  
  while q :
    x, y, dist = q.popleft()
    if dist == p_list[num] :
      next_list[idx].append((x, y))
      continue

    for k in range(4) :
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N and map_list[ay][ax] == '.' :
        map_list[ay][ax] = str(num+1)
        result[num] += 1
        q.append((ax, ay, dist+1))

  return len(next_list[idx]) == 0

next_list = [list() for _ in range(P)]
for i in range(N) :
  for j in range(M) :
    if '1' <= map_list[i][j] <= '9' :
      num = int(map_list[i][j]) - 1
      next_list[num].append((j, i))
      result[num] += 1

is_unchanged = [False]*P
idx = 0

while False in is_unchanged :
  if is_unchanged[idx] :
    idx = (idx + 1) % P
    continue
  is_unchanged[idx] = bfs(next_list, idx)
  idx = (idx + 1) % P
  
print(*result)