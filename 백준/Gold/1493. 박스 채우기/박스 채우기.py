import sys
input = sys.stdin.readline

L, W, H = map(int, input().split())
tot_volumn = L*W*H
N = int(input())
num_blocks = [0]*N
for _ in range(N) :
  i, a = map(int, input().split())
  num_blocks[i] = a

def div_and_con(l, w, h) :
  if l == 0 or w == 0 or h == 0 :
    return 0
  result = 0
  for i in range(N-1, -1, -1) :
    if not num_blocks[i] :
      continue
    boxlen = 2 ** i
    if not (l >= boxlen and w >= boxlen and h >= boxlen) :
      continue
    lnum, wnum = l // boxlen, w // boxlen
    if num_blocks[i] > lnum * wnum :
      base = lnum * wnum
    elif num_blocks[i] >= lnum :
      wnum = num_blocks[i] // lnum
      base = lnum * wnum
    else :
      wnum = 1
      lnum = num_blocks[i]
      base = num_blocks[i]

    num_blocks[i] -= base
    result += base
    left_l, left_w = l - lnum * boxlen, w - wnum * boxlen
    result += div_and_con(left_l, w, boxlen)
    result += div_and_con(l - left_l, left_w, boxlen)
    result += div_and_con(l, w, h - boxlen)
    return result
  return float('inf')

ans = div_and_con(L, W, H)
print(ans if ans < float('inf') else -1)