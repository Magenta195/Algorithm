from heapq import heappush, heappop
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
MAX = float('inf')

M, N = map(int, input().split())
map_list = [input().strip() for _ in range(N)]
visited = [[MAX]*M for _ in range(N)]
visited[0][0] = 0
q = [(0, 0, 0)]
while q :
  cnt, x, y = heappop(q)
  if x == M-1 and y == N-1 :
    print(cnt)
    break
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    if -1 < ax < M and -1 < ay < N :
      acnt = cnt + 1 if map_list[ay][ax] == '1' else cnt
      if visited[ay][ax] > acnt :
        visited[ay][ax] = acnt
        heappush(q, (acnt, ax, ay))