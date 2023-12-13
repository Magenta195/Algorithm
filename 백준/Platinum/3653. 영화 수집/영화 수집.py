import sys
input = sys.stdin.readline

class SegTree :
  def __init__(self, N, M) :
    self.size = N + M
    self.tree = [0]*(4*(N+M))
    self.loc = [-1]*N
    self.idx = N
    def _init(start, end, idx) :
      if start == end :
        if start < N :
          self.tree[idx] = 1
          self.loc[N-start-1] = start
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _init(0, self.size-1, 1)
  
  def update(self, target) :
    def _update(start, end, idx, target, val) :
      if end < target or start > target :
        return
      if start == end == target :
        self.tree[idx] = val
        return
      mid = (start + end) // 2
      _update(start, mid, idx*2, target, val)
      _update(mid+1, end, idx*2+1, target, val)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
      return
    target_idx = self.loc[target]
    _update(0, self.size-1, 1, target_idx, 0)
    _update(0, self.size-1, 1, self.idx, 1)
    self.loc[target] = self.idx
    self.idx += 1

  def search(self, target):
    target_idx = self.loc[target]
    def _search(start, end, idx) :
      if end < target_idx :
        return 0
      if target_idx <= start :
        return self.tree[idx]
      mid = (start + end) // 2
      return _search(start, mid, idx*2) + _search(mid+1, end, idx*2+1)

    print(_search(0, self.size-1, 1)-1, end = ' ')
        
def solve() :
  N, M = map(int, input().split())
  segtree = SegTree(N, M)
  for idx in map(int, input().split()) :
    segtree.search(idx-1)
    segtree.update(idx-1)
  print()
  
for _ in range(int(input())) :
  solve()