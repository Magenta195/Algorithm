from collections import defaultdict, deque
import sys
input = sys.stdin.readline
MAX = float('inf')

n, m, K = map(int, input().split())
jewelry = [0]*n
for i in range(K) :
  jewelry[int(input())-1] = i+1

edge_dict = defaultdict(list)
for _ in range(m) :
  a, b, c = map(int, input().split())
  edge_dict[a-1].append((b-1, c))
  edge_dict[b-1].append((a-1, c))

visited = [[False]*(1 << K) for _ in range(n)]
visited[0][0] = True
q = deque([(0, 0, 0)])
ans = 0

while q :
  node, cnt, visit = q.popleft()
  if node == 0 and visit :
    ans = max(ans, cnt)
    continue
  for nxt, cost in edge_dict[node] :
    if cost < cnt :
      continue
    if not visited[nxt][visit] :
      visited[nxt][visit] = True
      q.append((nxt, cnt, visit))
    if jewelry[nxt] :
      jidx = jewelry[nxt]-1
      if not visit & (1 << jidx) and not visited[nxt][visit | (1 << jidx)] :
        visited[nxt][visit | (1 << jidx)] = True
        q.append((nxt, cnt+1, visit | (1 << jidx)))
print(ans)