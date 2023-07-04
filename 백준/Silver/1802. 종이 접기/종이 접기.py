import sys
input = sys.stdin.readline

T = int(input())

def rev(s) :
  result = ''
  for _s in s[::-1] :
    result += str(1 - int(_s))
  return result

def origami(s) :
  if len(s) == 1 :
    return 1
  l = len(s) // 2
  left, right = s[:l], rev(s[l+1:])
  if left != right :
    return 0
  return origami(left)

for _ in range(T) :
  s = input().strip()
  result = origami(s)
  print('YES' if result else 'NO')