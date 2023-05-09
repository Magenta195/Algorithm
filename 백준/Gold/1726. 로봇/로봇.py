from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dd = [0, 1, 2, 1]
cd = [0, 2, 3, 1]
MAX = float('inf')

M, N = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(M)]
visited = [[[MAX]*4 for _ in range(N)] for _ in range(M)]

cvt = lambda x : int(x) - 1

sy, sx, sd = map(cvt, input().split())
ey, ex, ed = map(cvt, input().split())
sd, ed = cd[sd], cd[ed]
q = deque()
result = MAX
for k in range(4) :
  visited[sy][sx][(sd+k)%4] = dd[k]
  q.append((sx, sy, (sd+k)%4, dd[k]))

while q :
  x, y, d, dist = q.popleft()
  if (x, y) == (ex, ey) :
    result = min(result, dist + dd[abs(d - ed)])
    continue

  for k in range(4) :
    ad = (d + k) % 4
    next_dist = dist + 1 + dd[k]
    ax, ay = x + dx[ad], y + dy[ad]
    cnt = 0
    while -1 < ax < N and -1 < ay < M and cnt < 3 :
      if map_list[ay][ax] == 1 :
        break
      if visited[ay][ax][ad] > next_dist :
        visited[ay][ax][ad] = next_dist
        q.append((ax, ay, ad, next_dist))
      ax, ay = ax + dx[ad], ay + dy[ad]
      cnt += 1

print(result)