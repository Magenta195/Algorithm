import sys
input = sys.stdin.readline
MAX = 10**6
eps = 10**(-4)

def solve_cubic_eq(a, b, c, d) :
  idx = 1
  _range = []
  for i in range(1, int(abs(d)**0.5)+1) :
    if d % i == 0 :
      _range.append(i)
      _range.append(-i)
      if i != abs(d) // i :
        _range.append(abs(d) // i)
        _range.append(-abs(d) // i)
  
  for i in _range :
    if a*i**3 + b*i**2 + c*i + d == 0 :
      return i

def solve_quard_eq(a, b, c) :
  if b ** 2 - 4*a*c < 0 :
    return []
  elif b ** 2 - 4*a*c == 0 :
    return [-b / (2*a)]
  else :
    return [(-b + (b ** 2 - 4*a*c) ** 0.5) / (2*a), (-b - (b ** 2 - 4*a*c) ** 0.5) / (2*a) ]

def solve() :
  A, B, C, D = map(int, input().split())
  if D != 0 :
    a = solve_cubic_eq(A, B, C, D)
    b, c = B + a*A, -D / a
  else :
    a = 0
    b, c = B, C
  tmp = solve_quard_eq(A, b, c)
  ans = [a]
  for t in tmp :
    flg = True
    for _ans in ans :
      if abs(t - _ans) <= eps :
        flg = False
    if flg :
      ans.append(t)
  for _ans in sorted(ans) :
    print("{:.04f}".format(_ans), end = ' ')
  print()

for _ in range(int(input())) :
  solve()