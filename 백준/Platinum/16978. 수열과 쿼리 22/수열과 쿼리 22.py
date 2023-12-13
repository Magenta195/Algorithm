from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
search_q, update_q = list(), list()
sidx, uidx = 0, 0

for i in range(M) :
  q, *cmd = map(int, input().split())
  if q == 2 :
    search_q.append([sidx] + cmd)
    sidx += 1
  else :
    update_q.append([uidx] + cmd)
    uidx += 1

class SegTree :
  def __init__(self) :
    self.tree = [0]*(4*N)
    def _init(start, end, idx) :
      if start == end :
        self.tree[idx] = num_list[start]
        return
      mid = (start + end) // 2
      _init(start, mid, idx*2)
      _init(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _init(0, N-1, 1)

  def update(self, target, val) :
    def _update(start, end, idx) :
      if target < start or end < target :
        return
      if start == end :
        self.tree[idx] = val
        return
      mid = (start + end) // 2
      _update(start, mid, idx*2)
      _update(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _update(0, N-1, 1)

  def search(self, left, right) :
    def _search(start, end, idx) :
      if right < start or end < left :
        return 0
      if left <= start <= end <= right :
        return self.tree[idx]
      mid = (start + end) // 2
      l = _search(start, mid, idx*2)
      r = _search(mid+1, end, idx*2+1)
      return l + r
    return _search(0, N-1, 1)

search_q = deque(sorted(search_q, key = lambda x : x[1]))
ans = [0]*sidx
segtree = SegTree()
for uidx, idx, val in update_q :
  while search_q and search_q[0][1] == uidx :
    sidx, _, left, right = search_q.popleft()
    ans[sidx] = segtree.search(left-1, right-1)
  segtree.update(idx-1, val)
while search_q :
  sidx, _, left, right = search_q.popleft()
  ans[sidx] = segtree.search(left-1, right-1)

print(*ans, sep = '\n')