from random import randint
import sys
input = sys.stdin.readline

MAX = 20
N, C = map(int, input().split())
hats = list(map(int, input().split()))
M = int(input())

hatidx = [list() for _ in range(C+1)]
for i in range(N) :
  hatidx[hats[i]].append(i)

def cal(l, r, key) :
  lstart = rstart = 0
  lend = rend = len(hatidx[key])
  while lstart < lend :
    mid = (lstart + lend) // 2
    if hatidx[key][mid] < l :
      lstart = mid + 1
    else :
      lend = mid
  while rstart < rend :
    mid = (rstart + rend) // 2
    if hatidx[key][mid] <= r :
      rstart = mid + 1
    else :
      rend = mid
  return rend - lend

for _ in range(M) :
  l, r = map(lambda x : int(x)-1, input().split())
  K = r - l + 1
  flg = False
  for _ in range(MAX) :
    key = hats[randint(l, r)]
    if cal(l, r, key) > K / 2 :
      flg = True
      break
  if flg :
    print("yes", key)
  else :
    print("no")
