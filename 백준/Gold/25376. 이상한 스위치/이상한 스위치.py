from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
visited = [False]*(1 << N)
q = deque()

bulbs = list(map(int, input().split()))
init_bulb = 0
for i in range(N) :
  if bulbs[i] :
    init_bulb += 1 << i
changes = []
for _ in range(N) :
  _, *bulbs = map(int, input().split())
  tmp = 0
  for b in bulbs :
    tmp += 1 << (b - 1)
  changes.append(tmp)

q.append((init_bulb, 0))
visited[init_bulb] = True

flg = True
while q :
  b_visit, cnt = q.popleft()
  if b_visit == (1 << N) - 1 :
    flg = False
    print(cnt)
    break
  for i in range(N) :
    if b_visit & 1 << i :
      continue
    b_changed = (b_visit | 1 << i) ^ changes[i]
    if not visited[b_changed] :
      visited[b_changed] = True
      q.append((b_changed, cnt+1))

if flg :
  print(-1)