from collections import deque
import sys
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
MAX = float('inf')
N, T, R, C = map(int, input().split())
R -= 1
C -= 1
map_list = [input().strip() for _ in range(N)]
visited = [[[MAX]*2 for _ in range(N)] for _ in range(N)]
visited[0][0][0] = 0
q = deque([(0, 0, 0, 0)])

def warp(r, c, k) :
  r, c = r + dr[k], c + dc[k]
  while -1 < r < N and -1 < c < N :
    if map_list[r][c] == "#" :
      return (r, c)
    r += dr[k]
    c += dc[k]
  return (MAX, MAX)

while q :
  r, c, t, w = q.popleft()
  if (r, c) == (R, C) :
    continue
  for k in range(4) :
    ar, ac = r + dr[k], c + dc[k]
    if -1 < ar < N and -1 < ac < N and visited[ar][ac][0] > t + 1 :
      visited[ar][ac][0] = t + 1
      q.append((ar, ac, t+1, 0))
    wr, wc = warp(r, c, k)
    at = t + 1 if w else t + 1 + T
    if wr < MAX and visited[wr][wc][1] > at :
      visited[wr][wc][1] = at
      q.append((wr, wc, at, 1))

print(min(visited[R][C]))