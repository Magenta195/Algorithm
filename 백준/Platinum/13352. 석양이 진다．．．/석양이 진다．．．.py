import random
import sys
input = sys.stdin.readline

N = int(input())
coord_list = [tuple(map(int, input().split())) for _ in range(N)]
if N < 4 :
  print("success")
  exit()
def ccw(a, b, c) :
  return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def search(coord, ret) :
  next_coord = []
  for _coord in coord :
    if ccw(ret[-2], ret[-1], _coord) != 0 :
      next_coord.append(_coord)
  return next_coord

flg = False
for _ in range(10) :
  tmp = coord_list[:]
  for i in range(2) :
    ret = random.sample(tmp, 2)
    tmp = search(tmp, ret)
    if len(tmp) < 2-i :
      flg = True
      break
  if flg :
    break
print("success" if flg else "failure")