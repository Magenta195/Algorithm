import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
num_list = list(map(int, input().split()))

class SegTree() :
  def __init__(self) :
    self.tree = [0]*(4*N)
    self._init(1, 0, N-1)

  def _init(self, idx, start, end) :
    if start == end :
      self.tree[idx] = num_list[start]
      return

    mid = (start + end) // 2
    self._init(idx*2, start, mid)
    self._init(idx*2+1, mid+1, end)
    self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]

  def calculate(self, x, y) :
    if x > y :
      x, y = y, x
    return self._calculate(1, 0, N-1, x-1, y-1)

  def _calculate(self, idx, start, end, x, y) :
    if y < start or x > end :
      return 0
    if x <= start <= end <= y :
      return self.tree[idx]

    mid = (start + end) // 2
    left = self._calculate(idx*2, start, mid, x, y)
    right = self._calculate(idx*2+1, mid+1, end, x, y)
    return left + right
    
  def update(self, a, b) :
    self._update(1, 0, N-1, a-1, b)

  def _update(self, idx, start, end, target, val) :
    if target < start or target > end :
      return
    if start == end == target:
      self.tree[idx] = val
      return

    mid = (start + end) // 2
    self._update(idx*2, start, mid, target, val)
    self._update(idx*2+1, mid+1, end, target, val)
    self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]

segtree = SegTree()
for _ in range(Q) :
  x, y, a, b = map(int, input().split())
  print(segtree.calculate(x, y))
  segtree.update(a, b)