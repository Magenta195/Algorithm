import sys
input = sys.stdin.readline
MOD = 1000000007

T, N, D = map(int, input().split())
mat_list = list()

def matmul(a, b) :
  c = [[0]*N for _ in range(N)]

  for i in range(N) :
    for j in range(N) :
      for k in range(N) :
        c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % MOD

  return c

def matpow(a, p) :
  if p == 1 :
    return a

  b = matpow(a, p//2)
  b = matmul(b, b)
  if p % 2 == 0 :
    return b
  return matmul(b, a)

for _ in range(T) :
  mat = [[0]*N for _ in range(N)]
  t = int(input())
  for _ in range(t) :
    a, b, c = map(int, input().split())
    mat[a-1][b-1] = c
  if not mat_list :
    mat_list.append(mat)
  else :
    mat_list.append(matmul(mat_list[-1], mat))

m, r = D // T, D % T
ans = [[0]*N for _ in range(N)]

if m > 0 :
  ans = matpow(mat_list[-1], m)
  if r > 0 :
    ans = matmul(ans, mat_list[r-1])
elif r > 0 :
  ans = mat_list[r-1]

for _ans in ans :
  print(*_ans)