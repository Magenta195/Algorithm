import sys
input = sys.stdin.readline

N, T, Q = map(int, input().split())
tree = [1 for _ in range(4*N)]
lazy = [-1]*(4*N)

def propagate(start, end, idx) :
  if lazy[idx] == -1 :
    return
  if start < end :
    lazy[idx*2] = lazy[idx]
    lazy[idx*2+1] = lazy[idx]
  tree[idx] = 1 << lazy[idx]
  lazy[idx] = -1

def update(start, end, idx, left, right, val) :
  propagate(start, end, idx)
  if left > end or right < start :
    return
  if left <= start <= end <= right :
    lazy[idx] = val
    propagate(start, end, idx)
    return
  mid = (start + end) // 2
  update(start, mid, idx*2, left, right, val)
  update(mid+1, end, idx*2+1, left, right, val)
  tree[idx] = tree[idx*2] | tree[idx*2+1]

def query(start, end, idx, left, right) :
  propagate(start, end, idx)
  if left > end or right < start :
    return 0
  if left <= start <= end <= right :
    return tree[idx]
  mid = (start + end) // 2
  lres = query(start, mid, idx*2, left, right)
  rres = query(mid+1, end, idx*2+1, left, right)
  return lres | rres

for _ in range(Q) :
  q, *cmd = input().split()
  if q == 'C' :
    x, y, z = map(int, cmd)
    if x > y :
      x, y = y, x
    update(0, N-1, 1, x-1, y-1, z-1)
  else :
    x, y = map(int, cmd)
    if x > y :
      x, y = y, x
    print(bin(query(0, N-1, 1, x-1, y-1)).count('1'))