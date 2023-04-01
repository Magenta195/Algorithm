from collections import deque

F, S, G, U, D = map(int, input().split())

floor_visited = [float('inf')]*(F+1)
floor_visited[S] = 0

q = deque([(S, 0)])
flg = False

while q :
  now, cnt = q.popleft()
  if now == G :
    flg = True
    print(cnt)
    break
  for mv in [U, -D] :
    next_mv = now + mv
    if 0 < next_mv <= F and floor_visited[next_mv] > cnt + 1 :
      floor_visited[next_mv] = cnt + 1
      q.append((next_mv, cnt+1))

if not flg :
  print("use the stairs")