import sys
input = sys.stdin.readline

MOD = 10**9+7
N, K = map(int, input().split())
adj_mat = [list(map(int, input().split())) for _ in range(N)]

def matmul(A, B) :
  res = [[0]*N for _ in range(N)]
  for i in range(N) :
    for j in range(N) :
      for k in range(N) :
        res[i][j] = (res[i][j] + A[i][k]*B[k][j]) % MOD
  return res

def matpow(m, k) :
  if k == 1 :
    return m

  p = matpow(m, k//2)
  p = matmul(p, p)
  if k % 2 :
    p = matmul(p, m)
  return p

res = matpow(adj_mat, K)
print(sum(map(sum, res)) % MOD)