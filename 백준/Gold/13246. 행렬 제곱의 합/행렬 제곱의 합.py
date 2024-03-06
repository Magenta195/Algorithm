MOD = 1000
N, B = map(int, input().split())
mat = []
for _ in range(N) :
  _mat = list(map(lambda x : int(x) % MOD, input().split()))
  mat.append(_mat)

def matsum(A, B = None) :
  if B is None :
    B = [[0 if i != j else 1 for j in range(N)] for i in range(N)]
  return [[(A[i][j] + B[i][j]) % MOD for j in range(N)] for i in range(N)]

def matmul(A, B) :
  tmp = [[0]*N for _ in range(N)]
  for i in range(N) :
    for j in range(N) :
      for k in range(N) :
        tmp[i][j] = (tmp[i][j] + A[i][k] * B[k][j]) % MOD
  return tmp

def matpow(A, n) :
  if n == 1 :
    return A
  p = matpow(A, n // 2)
  p = matmul(p, p)
  if n % 2 :
    p = matmul(p, A)
  return p

def solve(m, b) :
  if b == 1 :
    return m
  lmat = solve(m, b // 2)
  rmat = matsum(matpow(m, b // 2))
  res = matmul(lmat, rmat)
  if b % 2 :
    res = matsum(res, matpow(m, b))
  return res

ans = solve(mat, B)
for _ans in ans :
  print(*_ans)