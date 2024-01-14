import math
N, K, M = map(int, input().split())
ans = 1
while N or K :
  ans = (ans * math.comb(N % M, K % M)) % M 
  N //= M
  K //= M
print(ans % M)