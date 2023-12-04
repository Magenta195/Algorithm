import sys
input = sys.stdin.readline
MAX = 10 ** 9
def extended_euclidean(a, b) :
  r1, r2 = a, b
  s1, s2 = 1, 0
  t1, t2 = 0, 1
  
  while r2 :
    q = r1 // r2
    r1, r2 = r2, r1 - q * r2
    s1, s2 = s2, s1 - q * s2
    t1, t2 = t2, t1 - q * t2
    
  return r1, s1, t1

def solve() :
  K, C = map(int, input().split())
  if K == 1 :
    print(1 if C > 1 else 2)
    return
  if C == 1 :
    print(K+1 if K < MAX else "IMPOSSIBLE")
    return
  gcd, _, ans = extended_euclidean(K, C)
  if gcd > 1 or ans > MAX:
    print("IMPOSSIBLE")
  else :
    print(ans if ans > 0 else K + ans)

for _ in range(int(input())) :
  solve()