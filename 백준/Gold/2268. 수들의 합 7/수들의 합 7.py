import sys
input = sys.stdin.readline
N, M = map(int, input().split())

class SegTree :
  def __init__(self) :
    self.tree = [0]*(N*4+1)

  def modify(self, i, k) :
    self._modify(0, N-1, 1, i-1, k)
    
  def _modify(self, start, end, idx, target, val) :
    if target < start or target > end :
      return
    if start == end == target :
      self.tree[idx] = val
      return

    mid = (start + end) // 2
    self._modify(start, mid, 2*idx, target, val)
    self._modify(mid+1, end, 2*idx+1, target, val)
    self.tree[idx] = sum(self.tree[2*idx:2*idx+2])

  def sum(self, i, j) :
    return self._sum(0, N-1, 1, i-1, j-1)

  def _sum(self, start, end, idx, l, r) :
    if l <= start <= end <= r :
      return self.tree[idx]
    if r < start or end < l :
      return 0

    mid = (start + end) // 2
    lval = self._sum(start, mid, 2*idx, l, r)
    rval = self._sum(mid+1, end, 2*idx+1, l, r)
    return lval + rval

segtree = SegTree()
for _ in range(M) :
  q, *cmd = map(int, input().split())
  if q == 0 :
    i, j = cmd
    if i > j :
      i, j = j, i
    print(segtree.sum(i, j))
  else :
    i, k = cmd
    segtree.modify(i, k)