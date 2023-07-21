from collections import deque, defaultdict
import sys

input = sys.stdin.readline
N, D = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
q = deque([(0, 0)])
result = D
while q :
  node, dist = q.popleft()
  if dist + D - node < result :
    result = dist + D - node
  for start, end, cost in map_list :
    if start < node or end > D :
      continue
    q.append((end, dist + start - node + cost))
    
print(result)