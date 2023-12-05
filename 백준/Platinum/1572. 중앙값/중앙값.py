import sys
input = sys.stdin.readline
MAX = 65537

N, K = map(int, input().split())
temp_list = [int(input()) for _ in range(N)]

class SegTree :
  def __init__(self, ):
    self.tree = [0]*(MAX*4)

  def update(self, temp, val) :
    self._update(0, MAX, 1, temp, val)

  def _update(self, start, end, idx, target, val) :
    if target < start or target > end :
      return
    self.tree[idx] += val
    if start == end :
      return
    mid = (start + end) // 2
    self._update(start, mid, idx*2, target, val)
    self._update(mid+1, end, idx*2+1, target, val)

  def search(self) :
    return self._search(0, MAX, 1, (K + 1) // 2 )

  def _search(self, start, end, idx, val) :
    if start == end :
      return start

    mid = (start + end) // 2
    left = self.tree[idx*2]
    if left >= val :
      return self._search(start, mid, idx*2, val)
    else :
      return self._search(mid+1, end, idx*2+1, val-left)


segtree = SegTree()
ans = 0

for i in range(N) :
  segtree.update(temp_list[i], 1)
  if i > K-1 :
    segtree.update(temp_list[i-K], -1)
  if i >= K-1 :
    ans += segtree.search()

print(ans)