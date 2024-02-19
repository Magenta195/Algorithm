import sys
input = sys.stdin.readline

N = int(input())
heights = sorted([int(input()) for _ in range(N)])
order = list(map(int, input().split()))

tree = [0]*(4*(N+1))
ans = [0] * N

def init(start, end, idx) :
  if start == end :
    tree[idx] = 1
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)
  tree[idx] = tree[idx*2] + tree[idx*2+1]

def search(target) :
  start, end, idx = 0, N-1, 1
  while start < end :
    tree[idx] -= 1
    mid = (start + end) // 2
    if tree[idx*2] < target :
      target -= tree[idx*2]
      start = mid + 1
      idx = idx*2 + 1
    else :
      end = mid
      idx = idx*2
  tree[idx] -= 1
  return end

init(0, N-1, 1)
for i, o in enumerate(reversed(order)) :
  idx = search(o+1)
  ans[N-i-1] = heights[idx]

print(*ans, sep = '\n')