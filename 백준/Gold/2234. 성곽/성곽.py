import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

M, N = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
area_list = list()

def dfs(x, y, num) :
  q = [(x, y)]
  result = 1
  
  while q :
    x, y = q.pop()
    for k in range(4) :
      if map_list[y][x] & (1 << k) : 
        continue
      ax, ay = x + dx[k], y + dy[k]
      if -1 < ax < M and -1 < ay < N and visited[ay][ax] == -1 :
        visited[ay][ax] = num
        q.append((ax, ay))
        result += 1

  area_list.append(result)

cnt = 0
for i in range(N) :
  for j in range(M) :
    if visited[i][j] == -1 :
      visited[i][j] = cnt
      dfs(j, i, cnt)
      cnt += 1
print(cnt)
print(max(area_list))

result = 0
for i in range(N) : 
  for j in range(M) :
    for k in range(4) :
      ai, aj = i + dy[k], j + dx[k]
      if -1 < aj < M and -1 < ai < N and visited[i][j] != visited[ai][aj] :
        result = max(result, area_list[visited[ai][aj]] + area_list[visited[i][j]])
print(result)
      