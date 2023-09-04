from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edge_dict = defaultdict(list)

for _ in range(M) :
  a, b = map(int, input().split())
  edge_dict[a-1].append(b-1)
  edge_dict[b-1].append(a-1)

dist_list = [float('inf')]*N
dist_list[0] = 0
q = deque([(0, 0)])

while q :
  node, dist = q.popleft()
  for nxt in edge_dict[node] :
    if dist_list[nxt] > dist + 1 :
      dist_list[nxt] = dist + 1
      q.append((nxt, dist + 1))

max_idx, max_dist, max_cnt = -1, -1, 0

for i in range(N) :
  if dist_list[i] > max_dist :
    max_idx, max_dist, max_cnt = i, dist_list[i], 1
  elif dist_list[i] == max_dist :
    max_cnt += 1
print(max_idx+1, max_dist, max_cnt)