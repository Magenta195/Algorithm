from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
q = list()
parents = list(range(N))
total = 0

for i in range(N) :
  maps = input().strip()
  for j in range(N) :
    if maps[j] != '0' :
      if ord(maps[j]) >= ord('a') :
        cable = ord(maps[j]) - ord('a') + 1
      else :
        cable = ord(maps[j]) - ord('A') + 27
      heappush(q, (cable, i, j))
      total += cable

def find(a) :
  if a == parents[a] :
    return a

  parents[a] = find(parents[a])
  return parents[a]

def union(pa, pb) :
  if pa < pb :
    parents[pb] = pa
  else :
    parents[pa] = pb

cnt = N-1
while q and cnt :
  cable, a, b = heappop(q)
  pa = find(a)
  pb = find(b)
  if pa != pb :
    union(pa, pb)
    cnt -= 1
    total -= cable

for i in range(N) :
  find(i)
parent_set = set(parents)
print(total if len(parent_set) < 2 else -1)