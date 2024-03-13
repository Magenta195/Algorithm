MOD = 10**9+7
N = int(input())
mat = [[2, 1], [1, 0]]

def matmul(a, b):
  c = [[0]*2 for _ in range(2)]
  for k in range(2) :
    for i in range(2) :
      for j in range(2) :
        c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % MOD
  return c

def matpow(m, p) :
  if p == 1 :
    return m
  _m = matpow(m, p//2)
  _m = matmul(_m, _m)
  if p % 2 :
    _m = matmul(_m, m)
  return _m

print(sum(matpow(mat, N)[0]) % MOD)