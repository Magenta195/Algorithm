import sys
input = sys.stdin.readline

N = int(input())
stars = list(map(int, input().split()))
Q = int(input())

class LazySegTree() :
  def __init__(self) :
    self.tree = [0]*(4*N)
    self.lazy = [[0, 0] for _ in range(4*N)]
    def _init(start, end, idx) :
      if start == end :
        self.tree[idx] = stars[start]
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)
    _init(0, N-1, 1)

  def propagate(self, start, end, idx) :
    if not self.lazy[idx][1] :
      return
    if start < end :
      mid = (start + end) // 2
      lmid = (mid + 1 - start) * self.lazy[idx][1] + self.lazy[idx][0]
      self.lazy[idx*2][0] += self.lazy[idx][0]
      self.lazy[idx*2][1] += self.lazy[idx][1]
      self.lazy[idx*2+1][0] += lmid
      self.lazy[idx*2+1][1] += self.lazy[idx][1]
    else :
      self.tree[idx] += self.lazy[idx][0]
    self.lazy[idx] = [0, 0]
   

  def update(self, L, R) :
    def _update(start, end, idx) :
      self.propagate(start, end, idx)
      if end < L or R < start :
        return
      if L <= start <= end <= R :
        self.lazy[idx][0] += start - L + 1
        self.lazy[idx][1] += 1
        self.propagate(start, end, idx)
        return
      mid = (start + end) // 2
      _update(start, mid, idx*2)
      _update(mid+1, end, idx*2+1)
    _update(0, N-1, 1)

  def search(self, x) :
    def _search(start, end, idx) :
      self.propagate(start, end, idx)
      if start == end == x :
        print(self.tree[idx])
        return
      if x < start or x > end :
        return
      mid = (start + end) // 2
      if x <= mid :
        _search(start, mid, idx*2)
      else :
        _search(mid+1, end, idx*2+1)
    _search(0, N-1, 1)

segtree = LazySegTree()
for _ in range(Q) :
  q, *cmd = map(int, input().split())
  if q == 1 :
    L, R = cmd
    segtree.update(L-1, R-1)
  else :
    x = cmd[0]
    segtree.search(x-1)