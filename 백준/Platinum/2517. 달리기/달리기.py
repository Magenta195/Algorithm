from collections import deque
import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
runners = [int(input()) for _ in range(N)]

class MergeSortTree :
  def __init__(self) :
    self.tree = [list() for _ in range(4*N)]
    def _init(start, end, idx) :
      if start == end :
        self.tree[idx] = [runners[start]]
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
      self.tree[idx].sort()
    _init(0, N-1, 1)

  def search(self, right) :
    val = runners[right]
    right -= 1
    def upper_bound(idx) :
      start, end = 0, len(self.tree[idx])
      while start < end :
        mid = (start + end) // 2
        if self.tree[idx][mid] <= val :
          start = mid + 1
        else :
          end = mid
      return len(self.tree[idx]) - end
    def _search(start, end, idx) :
      if right < start :
        return 0
      if start <= end <= right :
        return upper_bound(idx)
      mid = (start + end) // 2
      lval = _search(start, mid, idx*2)
      rval = _search(mid+1, end, idx*2+1)
      return lval + rval
    print(_search(0, N-1, 1) + 1)

tree = MergeSortTree()
for i in range(N) :
  tree.search(i)