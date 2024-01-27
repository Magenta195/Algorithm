import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, K = map(int, input().split())
civil_maps = [[0]*N for _ in range(N)]
civil = K
parents = list(range(K+1))

def find(a) :
  if a == parents[a] :
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(pa, pb) :
  if pa > pb :
    pa, pb = pb, pa
  parents[pb] = pa

def merge_civils(a, b) :
  global civil
  pa, pb = find(a), find(b)
  if pa != pb :
    civil -= 1
    union(pa, pb)

def bfs(q) :
  global civil
  next_q = []
  while q :
    x, y, c = q.pop()
    for i in range(4) :
      ax, ay = x + dx[i], y + dy[i]
      if not (-1 < ax < N and -1 < ay < N) :
        continue
      if civil_maps[ay][ax] :
        merge_civils(c, civil_maps[ay][ax])
        continue
      civil_maps[ay][ax] = c
      next_q.append((ax, ay, c))
      for j in range(4) :
        bx, by = ax + dx[j], ay + dy[j]
        if -1 < bx < N and -1 < by < N and civil_maps[by][bx] :
          merge_civils(c, civil_maps[by][bx])
  return next_q

q = []
cnt = 1
for _ in range(K) :
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  civil_maps[y][x] = cnt
  for i in range(4) :
    ax, ay = x + dx[i], y + dy[i]
    if -1 < ax < N and -1 < ay < N and civil_maps[ay][ax] :
      merge_civils(cnt, civil_maps[ay][ax])
  q.append((x, y, cnt))
  cnt += 1

t = 0
while civil > 1 :
  t += 1
  q = bfs(q)
print(t)