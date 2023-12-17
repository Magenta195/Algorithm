import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))

class MergeSortTree :
  def __init__(self) :
    self.tree = [list() for _ in range(4*N)]
    def _init(start, end, idx) :
      if start == end :
        self.tree[idx] = [num_list[start]]
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)

      l, r = 0, 0
      while l < mid-start+1 and r < end - mid :
        if self.tree[idx*2][l] > self.tree[idx*2+1][r] :
          self.tree[idx].append(self.tree[idx*2+1][r])
          r += 1
        else :
          self.tree[idx].append(self.tree[idx*2][l])
          l += 1
      while r < end - mid :
        self.tree[idx].append(self.tree[idx*2+1][r])
        r += 1
      while l < mid-start+1 :
        self.tree[idx].append(self.tree[idx*2][l])
        l += 1
    _init(0, N-1, 1)

  def search(self, left, right, val) :
    left -= 1
    right -= 1

    def upper_bound(start, end, idx) :
      while start < end :
        mid = (start + end) // 2
        if self.tree[idx][mid] <= val :
          start = mid + 1
        else :
          end = mid
      return len(self.tree[idx]) - end
    
    def _search(start, end, idx) :
      if right < start or left > end :
        return 0
      if left <= start <= end <= right :
        return upper_bound(0, end-start+1, idx)
      mid = (start + end) // 2
      lval = _search(start, mid, idx*2)
      rval = _search(mid+1, end, idx*2+1)
      return lval + rval

    print(_search(0, N-1, 1))

segtree= MergeSortTree()
for _ in range(int(input())) :
  i, j, k = map(int, input().split())
  segtree.search(i, j, k)