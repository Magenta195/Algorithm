N = int(input())
r, x = 0, 1

for _ in range(N) :
  a, b, _r = map(int, input().split())
  x = x * b // a
  r = r if _r == 0 else 1 - r

print(r, x)