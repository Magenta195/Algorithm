from collections import defaultdict, deque
import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
M = int(input())

edge_dict = defaultdict(list)
rev_edge_dict = defaultdict(list)

for _ in range(M) :
  a, b, c = map(int, input().split())
  edge_dict[a].append((b, c))
  rev_edge_dict[b].append((a, c))
S, E = map(int, input().split())

visited = [-MAX]*(N+1)
visited[S] = 0
q = deque([(S, 0)])
while q :
  node, dist = q.popleft()
  for nxt, ndist in edge_dict[node] :
    if visited[nxt] < dist + ndist :
      visited[nxt] = dist + ndist
      q.append((nxt, dist + ndist))

print(visited[E])
rev_visited = [False]*(N+1)
rev_visited[E] = True
ans = 0
q = deque([E])
while q :
  node = q.popleft()
  for prev, c in rev_edge_dict[node] :
    if visited[prev] + c != visited[node] :
      continue
    ans += 1
    if not rev_visited[prev] :
      rev_visited[prev] = True
      q.append(prev)
print(ans)