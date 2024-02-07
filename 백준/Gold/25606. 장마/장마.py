from collections import defaultdict
import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
rain = list(map(int, input().split()))

sums = [0]*N
evap = [0]*N
q = defaultdict(lambda : [0, 0])
cnt = 0

for i in range(N) :
  sums[i] = rain[i]
  if i > 0 :
    sums[i] += sums[i-1]
  if i in q :
    evap[i] += q[i][1]
    cnt -= q[i][0]
    del q[i]
  evap[i] += cnt * M
  q[i+1+rain[i]//M][0] += 1
  q[i+1+rain[i]//M][1] += rain[i] % M
  cnt += 1
  
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