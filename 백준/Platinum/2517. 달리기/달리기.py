from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
runners = [int(input()) for _ in range(N)]
rank = sorted(runners)
runners = [bisect_left(rank, r) for r in runners]

class SegTree :
  def __init__(self) :
    self.tree = [0]*(4*N)
    
  def update(self, target) :
    def _update(start, end, idx) :
      if start == end :
        self.tree[idx] += 1
        return
      mid = (start + end) // 2
      if target <= mid :
        _update(start, mid, idx*2)
      else :
        _update(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _update(0, N-1, 1)
  
  def search(self, target, order) :
    start, end, idx, val = 0, N-1, 1, 0
    while start < end :
      mid = (start + end) // 2
      if target >= mid :
        start = mid + 1
        val += self.tree[idx*2]
        idx = idx*2+1
      else :
        end = mid
        idx = idx*2
    print(order + 1 - val)

tree = SegTree()
for i in range(N) :
  tree.search(runners[i], i)
  tree.update(runners[i])