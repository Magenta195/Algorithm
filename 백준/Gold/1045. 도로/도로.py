from heapq import *
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = 0
edge_q = []
left_q = []
node_cnt = N-1
ans = [0]*N

for i in range(N) :
  maps = input().strip()
  for j in range(i+1, N) :
    if maps[j] == 'Y' :
      heappush(edge_q, (i, j))

parents = list(range(N))

def find(a) :
  if parents[a] == a :
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(pa, pb) :
  if pa > pb :
    pa, pb = pb, pa
  parents[pb] = pa

while edge_q and cnt < M :
  a, b = heappop(edge_q)
  pa, pb = find(a), find(b)
  if pa == pb :
    heappush(left_q, (a, b))
    continue
  union(pa, pb)
  cnt += 1
  ans[a] += 1
  ans[b] += 1

if cnt < N-1 :
  print(-1)
  exit()

while left_q and cnt < M :
  a, b = heappop(left_q)
  ans[a] += 1
  ans[b] += 1
  cnt += 1
print(*(ans if cnt == M else [-1]))