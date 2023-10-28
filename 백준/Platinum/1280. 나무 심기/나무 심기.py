N = int(input())
MAXVAL = 200000
MOD = 1000000007
num_list = [int(input()) for _ in range(N)]

class SegTree() :
  def __init__(self) :
    self.tree = [[0]*2 for _ in range(4*MAXVAL)]

  def search(self, val) :
    l, r = (0, 0), (0, 0)
    if val > 0 :
      l = self._search(1, 0, MAXVAL, 0, val-1)
    if val < MAXVAL :
      r = self._search(1, 0, MAXVAL, val+1, MAXVAL)

    result = (val*l[0] - l[1]) + (r[1] - val*r[0])
    return result % MOD

  def _search(self, idx, start, end, l, r) :
    if end < l or r < start :
      return 0, 0
    if l <= start and end <= r :
      return self.tree[idx]

    mid = (start + end) // 2
    left = self._search(2*idx, start, mid, l, r)
    right = self._search(2*idx+1, mid+1, end, l, r)

    return (left[0] + right[0]) % MOD, (left[1] + right[1]) % MOD

  def update(self, val) :
    self._update(1, 0, MAXVAL, val)

  def _update(self, idx, start, end, val) :
    if end < val or val < start :
      return
    if start == end :
      self.tree[idx][0] = (self.tree[idx][0] + 1) % MOD
      self.tree[idx][1] = (self.tree[idx][1] + start) % MOD
      return

    mid = (start + end) // 2
    self._update(2*idx, start, mid, val)
    self._update(2*idx+1, mid+1, end, val)

    self.tree[idx][0] = ( self.tree[2*idx][0] + self.tree[2*idx+1][0] ) % MOD
    self.tree[idx][1] = ( self.tree[2*idx][1] + self.tree[2*idx+1][1] ) % MOD


ans = 1
segtree = SegTree()
segtree.update(num_list[0])
for i in range(1, N) :
  ans = (ans * segtree.search(num_list[i])) % MOD
  segtree.update(num_list[i])

print(ans)