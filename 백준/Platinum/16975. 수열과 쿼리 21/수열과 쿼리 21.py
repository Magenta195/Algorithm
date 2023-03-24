import sys
input = sys.stdin.readline

class Seg_tree() :
  def __init__(self, length, val_list) :
    self.tree = [0]*(length*4)
    self.lazy = [0]*(length*4)
    self.val_list = val_list
    self.length = length
    
    start, end = 1, self.length
    self._init(1, start, end)

  def _init(self, node, start, end) :
    if start == end :
      self.tree[node] = self.val_list[start]
      return
    mid = (start + end) // 2
    self._init(node*2, start, mid)
    self._init(node*2 + 1, mid+1, end)

  def _propagate(self, node, start, end) :
    if self.lazy[node] != 0 :
      if start != end :
        self.lazy[node*2] += self.lazy[node]
        self.lazy[node*2 + 1] += self.lazy[node]
      else :
        self.tree[node] += self.lazy[node]
      self.lazy[node] = 0
        
  
  def update(self, l, r, val) :
    start, end = 1, self.length
    self._update(1, start, end, l, r, val)
  
  def _update(self, node, start, end, l, r, val) :
    self._propagate(node, start, end)
    if l > end or r < start :
      return

    if l <= start and end <= r :
      self.lazy[node] += val
      self._propagate(node, start, end)
      return
      
    if self.lazy[node] != 0 :
      self.lazy[node*2] += self.lazy[node]
      self.lazy[node*2 + 1] += self.lazy[node]
      self.lazy[node] = 0
      
    mid = (start + end) // 2
    self._update(node*2, start, mid, l, r, val)
    self._update(node*2+1, mid+1, end, l, r, val)

  def out(self, target) :
    start, end = 1, self.length
    return self._out(1, start, end, target)
    
  def _out(self, node, start, end, target) :
    self._propagate(node, start, end)
    
    if target == start == end :
      return self.tree[node]
    if target < start or target > end :
      return 0

    mid = (start + end) // 2
    if target <= mid :
      return self._out(node*2, start, mid, target)
    else :
      return self._out(node*2+1, mid+1, end, target)

def solve() :
  N = int(input())
  val_list = [0] + list(map(int, input().split()))
  M = int(input())
  seg_tree = Seg_tree(N, val_list)

  for _ in range(M) :
    q, *commands = map(int, input().split())
    if q == 1 :
      i, j, val = commands
      seg_tree.update(i, j, val)
    else :
      target = commands[0]
      print(seg_tree.out(target))

solve()