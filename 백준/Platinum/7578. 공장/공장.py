import sys
input = sys.stdin.readline
MAX = 1000001

N = int(input())

class SegTree() :
  def __init__(self) :
    self.node = [0]*(4*N)

  def search(self, target) :
    return self._search(1, target+1, N-1, 0, N-1)
    
  def _search(self, idx, l, r, start, end) :
    if r < start or l > end :
      return 0
    if l <= start <= end <= r :
      return self.node[idx]

    mid = (start + end) // 2
    left = self._search(idx*2, l, r, start, mid)
    right = self._search(idx*2+1, l, r, mid+1, end)
    return left + right

    
  def update(self, target) :
    self._update(1, target, 0, N-1)

  def _update(self, idx, target, start, end) :
    if start == end == target :
      self.node[idx] = 1
      return
    if target < start or target > end :
      return

    mid = (start + end) // 2
    self._update(idx*2, target, start, mid)
    self._update(idx*2+1, target, mid+1, end)
    self.node[idx] = self.node[2*idx] + self.node[2*idx+1]

hashmap = [0]*MAX
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
ans = 0
segtree = SegTree()

for i, n in enumerate(b_list) :
  hashmap[n] = i
for n in a_list :
  idx = hashmap[n]
  ans += segtree.search(idx)
  segtree.update(idx)
print(ans)