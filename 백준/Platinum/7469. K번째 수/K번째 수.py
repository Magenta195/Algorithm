import bisect
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 10**9
nums = list(map(int, input().split()))

tree = [list() for _ in range(4*N)]

def init(start = 0, end = N-1, idx = 1) :
  if start == end :
    tree[idx] = [nums[start]]
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)
  tree[idx] = tree[idx*2] + tree[idx*2+1]
  tree[idx].sort()

def search(left, right, target) :
  idx_list = []
  def _search(start, end, idx) :
    if right < start or left > end :
      return
    if left <= start <= end <= right :
      idx_list.append(idx)
      return
    mid = (start + end) // 2
    _search(start, mid, idx*2)
    _search(mid+1, end, idx*2+1)

  _search(0, N-1, 1)
  start, end = -MAX, MAX
  ans = start
  while start < end :
    mid = (start + end) // 2
    cur = 0
    for idx in idx_list :
      cur += bisect.bisect_left(tree[idx], mid)
    if cur > target :
      end = mid
    else :
      ans = mid
      start = mid + 1
  print(ans)

init()
for _ in range(M) :
  i, j, k = map(int, input().split())
  search(i-1, j-1, k-1)