import sys
input = sys.stdin.readline
MAX = 10**5

N = int(input())
tree = [0]*(4*MAX+4)
lazy = [0]*(4*MAX+4)

def propagate(start, end, idx) :
  if start != end :
    lazy[idx*2] += lazy[idx]
    lazy[idx*2+1] += lazy[idx]
  else :
    tree[idx] += lazy[idx]
  lazy[idx] = 0

def update(l, r, start=0, end=MAX, idx=1) :
  if l > r :
    return
  propagate(start, end, idx)
  if l > end or r < start :
    return
  if l <= start <= end <= r :
    lazy[idx] += 1
    propagate(start, end, idx)
    return
  mid = (start + end) // 2
  update(l, r, start, mid, idx*2)
  update(l, r, mid+1, end, idx*2+1)

def search(target) :
  start, end, idx = 0, MAX, 1
  while start < end :
    propagate(start, end, idx)
    mid = (start + end) // 2
    if target <= mid :
      end = mid
      idx = idx*2
    else :
      start = mid+1
      idx = idx*2+1
  propagate(start, end, idx)
  result = tree[idx] 
  tree[idx] = 0
  return result

for _ in range(N) :
  L, R = map(int, input().split())
  print(search(L) + search(R))
  update(L+1, R-1)