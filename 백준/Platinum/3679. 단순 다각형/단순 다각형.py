import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(a, b, c) :
  return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def dist(a, b) :
  return sum([(a[i]-b[i])**2 for i in range(2)])

def cmp(a, b) :
  if ccw(ref, a, b) > 0 :
    return 1
  if ccw(ref, a, b) == 0 and dist(ref, a) > dist(ref, b) :
    return 1
  return -1

def solve() :
  global ref
  N, *raw = map(int, input().split())

  points = list()
  ref = (10001, 10001, -1)
  for i in range(N) :
    p = (raw[2*i], raw[2*i+1], i)
    points.append(p)
    if ref > p :
      ref = p
  points.sort(key = cmp_to_key(cmp))
  last, last_ref = list(), points[-1]

  ans = [ref[2]]
  for p in points :
    if p == ref :
      continue
    if ccw(ref, last_ref, p) == 0 :
      last.append(p)
    else :
      ans.append(p[2])
  for _, _, i in reversed(last) :
    ans.append(i)
  print(*ans)

for _ in range(int(input())) :
  solve()