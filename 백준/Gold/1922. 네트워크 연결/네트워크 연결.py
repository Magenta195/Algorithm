from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parents = list(range(N))

def find(a) :
  if a == parents[a] :
    return a
  parents[a] = find(parents[a])
  return parents[a]

def union(pa, pb) :
  if pa > pb :
    parents[pa] = pb
  else :
    parents[pb] = pa

q = list()
for _ in range(M) :
  a, b, c = map(int, input().split())
  heappush(q, (c, a-1, b-1))

ans = 0
left = N-1
while q and left: 
  c, a, b = heappop(q)
  pa = find(a)
  pb = find(b)
  if pa != pb :
    union(pa, pb)
    ans += c
    left -= 1
print(ans)