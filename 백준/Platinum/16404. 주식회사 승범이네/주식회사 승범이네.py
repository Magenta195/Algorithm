from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N, M = map(int, input().split())
parent = list(map(int, input().split()))
children = defaultdict(list)

for i in range(1, N) :
  children[parent[i]-1].append(i)

employee_info = [[0]*2 for _ in range(N)]
eidx = -1
def dfs(node) :
  global eidx
  eidx += 1
  employee_info[node][0] = eidx
  for child in children[node] :
    dfs(child)
  employee_info[node][1] = eidx

class LazySegTree :
  def __init__(self) :
    self.tree = [0]*(4*N)
    self.lazy = [0]*(4*N)

  def propagate(self, start, end, idx) :
    if start != end :
      self.lazy[idx*2] += self.lazy[idx]
      self.lazy[idx*2+1] += self.lazy[idx]
    else :
      self.tree[idx] += self.lazy[idx]
    self.lazy[idx] = 0

  def update(self, left, right, val) :
    def _update(start, end, idx) :
      self.propagate(start, end, idx)
      if right < start or left > end :
        return
      if left <= start <= end <= right :
        self.lazy[idx] += val
        self.propagate(start, end, idx)
        return
      mid = (start + end) // 2
      _update(start, mid, idx*2)
      _update(mid+1, end, idx*2+1)
    _update(0, N-1, 1)

  def search(self, target) :
    start, end, idx = 0, N-1, 1
    while start < end :
      self.propagate(start, end, idx)
      mid = (start + end) // 2
      if target <= mid :
        end = mid
        idx *= 2
      else :
        start = mid+1
        idx = idx*2+1
    self.propagate(start, end, idx)
    print(self.tree[idx])

dfs(0)
tree = LazySegTree()
for _ in range(M) :
  q, *cmd = map(int, input().split())
  if q == 1 :
    i, val = cmd
    l, r = employee_info[i-1]
    tree.update(l, r, val)
  else :
    i = cmd[0]
    i = employee_info[i-1][0]
    tree.search(i)