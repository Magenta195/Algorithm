from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, C = map(int, input().split())
edge_dict = defaultdict(list)
visited = [False]*N
node_info = [[0]*3 for _ in range(N)]
idx = -1

for _ in range(N-1) :
  x, y = map(int, input().split())
  edge_dict[x-1].append(y-1)
  edge_dict[y-1].append(x-1)

def dfs(node, depth) :
  global idx
  visited[node] = True
  idx += 1
  node_info[node][0] = idx
  node_info[node][2] = depth

  for child in edge_dict[node] :
    if not visited[child] :
      dfs(child, depth+1)
  node_info[node][1] = idx

class SegTree() :
  def __init__(self) :
    self.tree = [0]*(4*N)

  def update(self, target) :
    target = node_info[target][0]
    def _update(start, end, idx) :
      if target < start or target > end :
        return
      if start == end :
        self.tree[idx] += 1
        return
      mid = (start + end) // 2
      _update(start, mid, idx*2)
      _update(mid+1, end, idx*2+1)
      self.tree[idx] = self.tree[idx*2] + self.tree[idx*2+1]
    _update(0, N-1, 1)

  def search(self, target) :
    left, right, mul = node_info[target]
    def _search(start, end, idx) :
      if right < start or left > end :
        return 0
      if left <= start <= end <= right :
        return self.tree[idx]
      mid = (start + end) // 2
      lval = _search(start, mid, idx*2)
      rval = _search(mid+1, end, idx*2+1)
      return lval + rval
    print(_search(0, N-1, 1) * mul)

tree = SegTree()
dfs(C-1, 1)
for _ in range(int(input())) :
  q, c = map(int, input().split())
  if q == 1 :
    tree.update(c-1)
  else :
    tree.search(c-1)