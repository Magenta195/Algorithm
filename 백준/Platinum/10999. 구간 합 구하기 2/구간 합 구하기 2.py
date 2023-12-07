import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
num_list = [int(input()) for _ in range(N)]

class LazySegTree() :
  def __init__(self) :
    self.tree = [0]*(4*N)
    self.lazy = [0]*(4*N)
    def _init(start, end, idx) :
      if start == end :
        self.tree[idx] = num_list[start]
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]

    _init(0, N-1, 1)

  def lazy_propagate(self, idx, start, end) :
    self.tree[idx] += self.lazy[idx] * (end - start + 1)
    if start < end :
      self.lazy[idx*2] += self.lazy[idx]
      self.lazy[idx*2+1] += self.lazy[idx]
    self.lazy[idx] = 0

  def update(self, left, right, val) :
    def _update(start, end, idx) :
      self.lazy_propagate(idx, start, end)
      if end < left or start > right :
        return
      if left <= start <= end <= right :
        self.lazy[idx] += val
        self.lazy_propagate(idx, start, end)
        return
      mid = (start + end) // 2
      _update(start, mid, idx*2)
      _update(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]

    _update(0, N-1, 1)

  def search(self, left, right) :
    def _search(start, end, idx) :
      self.lazy_propagate(idx, start, end)
      if end < left or start > right :
        return 0
      if left <= start <= end <= right :
        return self.tree[idx]
      mid = (start + end) // 2
      result = 0
      result += _search(start, mid, idx*2)
      result += _search(mid+1, end, idx*2+1)
      return result

    print(_search(0, N-1, 1))

segtree = LazySegTree()

for _ in range(M+K) :
  op, *cmd = map(int, input().split())
  if op == 1 :
    start, end, val = cmd
    segtree.update(start-1, end-1, val)
  else :
    start, end = cmd
    segtree.search(start-1, end-1)