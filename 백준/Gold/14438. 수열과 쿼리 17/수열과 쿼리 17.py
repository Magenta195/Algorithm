import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
nums = list(map(int, input().split()))
tree = [MAX]*(4*N)

def init(start, end, idx) :
  if start == end :
    tree[idx] = nums[start]
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)
  tree[idx] = min(tree[idx*2], tree[idx*2+1])

def update(start, end, idx, target, val) :
  if start > target or end < target :
    return
  if start == end :
    tree[idx] = val
    return
  mid = (start + end) // 2
  update(start, mid, idx*2, target, val)
  update(mid+1, end, idx*2+1, target, val)
  tree[idx] = min(tree[idx*2], tree[idx*2+1])

def search(start, end, idx, left, right) :
  if right < start or end < left :
    return MAX
  if left <= start <= end <= right :
    return tree[idx]
  mid = (start + end) // 2
  lval = search(start, mid, idx*2, left, right)
  rval = search(mid+1, end, idx*2+1, left, right)
  return min(lval, rval)

init(0, N-1, 1)
M = int(input())
for _ in range(M) :
  q, i, j = map(int, input().split())
  if q == 1  :
    update(0, N-1, 1, i-1, j)
  else :
    print(search(0, N-1, 1, i-1, j-1))
