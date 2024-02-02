from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
orth_dict = defaultdict(int)
zeros = 0
ans = 0

def gcd(a, b) :
  while b :
    a, b = b, a%b
  return a

for _ in range(N) :
  x, y = map(int, input().split())
  if x == y == 0 :
    zeros += 1
    continue
  if x == 0 :
    y = 1
  elif y == 0 :
    x = 1
  else :
    g = gcd(abs(x), abs(y))
    x, y = x // g, y // g
  if (x, y) in orth_dict :
    ans += orth_dict[(x, y)]
  for t in [(-y, x), (y, -x)] :
    orth_dict[t] += 1

print(ans + zeros * (N-zeros) + (zeros * (zeros-1) // 2))