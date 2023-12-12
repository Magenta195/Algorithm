MOD = 1000000007
N, R = map(int, input().split())
num = 1
a, b = 1, 1
for i in range(1, N+1) :
  num = (num * i) % MOD
  if i == N :
    a = (a * num) % MOD
  if i == R :
    b = (b * num) % MOD
  if i == N-R :
    b = (b * num) % MOD
    
def extend_euclidean(n) :
  a, b = n, MOD
  x0, x1 = 1, 0
  y0, y1 = 0, 1

  while b :
    q = a // b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1
    a, b = b, a % b
  if x0 < 0 :
    x0 += MOD
    
  return x0

print(a * extend_euclidean(b) % MOD)