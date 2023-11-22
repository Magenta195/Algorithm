import sys
input = sys.stdin.readline

N, M = map(int, input().split())

s, t = float('inf'), float('inf')
for _ in range(M) :
  _s, _t = map(int, input().split())
  s = min(s, _s)
  t = min(t, _t)

if s >= t*6 :
  print(t * N)
else :
  print(s * (N // 6) + min(s, t * (N % 6))) 