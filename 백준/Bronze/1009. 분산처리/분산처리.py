import sys
input = sys.stdin.readline

def mod(a, b) :
  if b == 1 :
    return a % 10

  p = mod(a, b // 2) % 10
  p = (p * p) % 10
  if b % 2 :
    return (p * a) % 10
  return p

for i in range(int(input())) :
  a, b = map(int, input().split())
  result = mod(a, b)
  print(result if result else 10)