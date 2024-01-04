from collections import deque
import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
M = int(input())
visited = [MAX]*(N+1)
q = deque()

for n in map(int, input().split()) :
  visited[n] = 0
  q.append((n, 0, 0))

while q :
  n, cnt, changed = q.popleft()
  for i in range(21) :
    var = n ^ (1 << i)
    if changed & (1 << i) or var > N :
      continue
    if visited[var] > cnt + 1 :
      visited[var] = cnt + 1
      q.append((var, cnt + 1, changed | (1 << i)))

print(max(visited))