import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
MAX = float('inf')
class SegTree :
  def __init__(self) :
    self.nodes = [0]*(4*N)
    self.init(1, N, 1)

  def init(self, start, end, idx) :
    if start == end :
      self.nodes[idx] = nums[start-1]
      return self.nodes[idx]
    mid = (start + end) // 2
    l = self.init(start, mid, idx*2)
    r = self.init(mid+1, end, idx*2+1)
    self.nodes[idx] = min(l, r)
    return self.nodes[idx]

  def cal(self, start, end, l, r, idx) :
    if r < start or end < l :
      return MAX
    if l <= start <= end <= r :
      return self.nodes[idx]
    mid = (start + end) // 2
    lval = self.cal(start, mid, l, r, idx*2)
    rval = self.cal(mid+1, end, l, r, idx*2+1)
    return min(lval, rval)

segtree = SegTree()
for _ in range(M) :
  a, b = map(int, input().split())
  print(segtree.cal(1, N, a, b, 1))