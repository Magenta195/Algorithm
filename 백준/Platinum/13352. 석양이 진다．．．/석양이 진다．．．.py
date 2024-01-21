import random
import sys
input = sys.stdin.readline

N = int(input())
coord_list = [list(map(int, input().split())) + [i] for i in range(N)]

def ccw(a, b, c) :
  return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])

def search(coord) :
  next_coord = []
  ret = coord[:2]
  for x, y, i in coord[2:] :
    if ccw(ret[-2], ret[-1], (x, y)) != 0 :
      next_coord.append([x, y, i])
  return next_coord

flg = False
for _ in range(10) :
  idx = list(range(N))
  random.shuffle(idx)
  tmp = sorted(coord_list, key = lambda x : idx[x[-1]])
  
  for _ in range(2) :
    tmp = search(tmp)
    if not tmp :
      flg = True
      break
  if flg :
    break
print("success" if flg else "failure")