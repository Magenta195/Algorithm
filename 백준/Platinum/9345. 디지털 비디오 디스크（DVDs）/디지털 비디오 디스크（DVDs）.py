import sys
import math
input = sys.stdin.readline

class SegTree :
  def __init__(self, N) :
    self.sz = 1 << math.ceil(math.log2(N))
    self.tree = [[0, 0] for _ in range(2*self.sz)]
    
    for i in range(self.sz) :
      if i < N :
        self.tree[i + self.sz] = [i, i]
      else :
        self.tree[i + self.sz] = [self.sz, -1]
    for i in range(self.sz-1, 0, -1) :
      self.tree[i][0] = min(self.tree[i<<1][0], self.tree[i<<1|1][0])
      self.tree[i][1] = max(self.tree[i<<1][1], self.tree[i<<1|1][1])

  def search(self, left, right) :
    left += self.sz
    right += self.sz
    ret = [self.sz, -1]
    while left <= right :
      if left % 2 == 1 :
        ret[0] = min(ret[0], self.tree[left][0])
        ret[1] = max(ret[1], self.tree[left][1])
        left += 1
      if right % 2 == 0 :
        ret[0] = min(ret[0], self.tree[right][0])
        ret[1] = max(ret[1], self.tree[right][1])
        right -= 1
      left >>= 1
      right >>= 1
    return ret
    
  def update(self, aidx, bidx) :
    aidx += self.sz
    bidx += self.sz
    def _update(idx) :
      while idx > 1 :
        idx >>= 1
        self.tree[idx][0] = min(self.tree[idx<<1][0], self.tree[idx<<1|1][0])
        self.tree[idx][1] = max(self.tree[idx<<1][1], self.tree[idx<<1|1][1])
    for i in range(2) :
      self.tree[aidx][i], self.tree[bidx][i] = self.tree[bidx][i], self.tree[aidx][i]
    _update(aidx)
    _update(bidx)

def solve() :
  N, K = map(int, input().split())
  tree = SegTree(N)
  for _ in range(K) :
    q, a, b = map(int, input().split())
    if q == 0 :
      tree.update(a, b)
    else :
      aval, bval = tree.search(a, b)
      if aval == a and bval == b :
        print("YES")
      else :
        print("NO")

for _ in range(int(input())) :
  solve()