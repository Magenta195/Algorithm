from heapq import *

K, N = map(int, input().split())
prime_num = list(map(int, input().split()))
q = prime_num[:]
heapify(q)

for _ in range(N) :
  num = heappop(q)
  for p in prime_num :
    heappush(q, num*p)
    if num % p == 0 :
      break
      
print(num)