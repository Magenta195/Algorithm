from heapq import *
import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
rain = list(map(int, input().split()))

sums = [0]*N
evap = [0]*N
q = []
for i in range(N) :
  sums[i] = rain[i]
  if i > 0 :
    sums[i] += sums[i-1]
  while q and q[0][0] <= i :
    _, left = heappop(q)
    evap[i] += left
  evap[i] += len(q) * M
  heappush(q, (i + rain[i] // M + 1, rain[i] % M))
  
for i in range(1, N) :
  evap[i] += evap[i-1]

for _ in range(Q) :
  q, c = map(int, input().split())
  if q == 1 :
    print(sums[c-1] - evap[c-1])
  elif c > 1 :
    print(evap[c-1] - evap[c-2])
  else :
    print(evap[c-1])