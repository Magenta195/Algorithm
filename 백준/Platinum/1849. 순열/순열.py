import sys
input = sys.stdin.readline

N = int(input())

class SegTree :
  def __init__(self) :
    self.tree = [0]*(4*N)
    self.result = [0]*N
    self.index = 1
    def _init(start, end, idx) :
      if start == end :
        self.tree[idx] = 1
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _init(0, N-1, 1)

  def search(self, rank) :
    start, end, idx = 0, N-1, 1
    while start < end :
      mid = (start + end) // 2
      if self.tree[idx*2] > rank :
        end = mid
        idx = idx*2
      else :
        start = mid + 1
        rank -= self.tree[idx*2]
        idx = idx*2+1
    return end

  def update(self, target) :
    start, end, idx = 0, N-1, 1
    self.tree[idx] -= 1
    while start < end :
      mid = (start + end) // 2
      if mid >= target :
        end = mid
        idx = idx*2
      else :
        start = mid + 1
        idx = idx*2+1
      self.tree[idx] -= 1
    self.result[target] = self.index
    self.index += 1

segtree = SegTree()
for _ in range(N) :
  num = int(input())
  target = segtree.search(num)
  segtree.update(target)
print(*segtree.result, sep = '\n')
