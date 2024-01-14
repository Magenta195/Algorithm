import sys
sys.setrecursionlimit(5000)

N, K, M = map(int, input().split())
ans = 1

cb = [[-1]*(M+1) for _ in range(M+1)]
def comb(n, k) :
  if n < k :
    return 0
  if k == n or k == 0:
    return 1
  if cb[n][k] > -1 :
    return cb[n][k]
  cb[n][k] = comb(n-1, k-1) + comb(n-1, k)
  return cb[n][k]

while N or K :
  ans = (ans * comb(N % M, K % M)) % M
  N //= M
  K //= M
print(ans % M)