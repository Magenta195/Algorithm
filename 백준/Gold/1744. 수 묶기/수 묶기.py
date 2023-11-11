from heapq import *

N = int(input())
neg, pos = list(), list()

for _ in range(N) :
  x = int(input())
  if x <= 0 :
    heappush(neg, x)
  else :
    heappush(pos, -x)

ans = 0
while len(pos) > 1 :
  a = -heappop(pos)
  b = -heappop(pos)
  if a*b > a + b :
    ans += a*b
  else :
    ans += a + b
while pos :
  ans += -heappop(pos)

while len(neg) > 1 :
  a = heappop(neg)
  b = heappop(neg)
  if a*b > a + b :
    ans += a * b
  else :
    ans += a + b
while neg :
  ans += heappop(neg)

print(ans)