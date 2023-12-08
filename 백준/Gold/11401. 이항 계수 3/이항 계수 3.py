N, K = map(int, input().split())
MOD = 1000000007
fac = [0]*(N+1)
fac[0] = 1
for i in range(1, N+1):
  fac[i] = (fac[i-1]*i)%MOD

def pw(n, t):
  if t == 0 : return 1
  if t == 1 : return n
  p = pw(n, t//2) % MOD
  p = (p*p) % MOD
  if t%2 == 0 :
    return p
  else :
    return (p*n) % MOD

print((fac[N]*pw(fac[K]*fac[N-K], MOD-2))%MOD)

