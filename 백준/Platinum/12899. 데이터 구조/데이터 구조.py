import sys
input = sys.stdin.readline
MAX = 2000000
tree = [0]*(4*MAX+4)

def update(target) :
  start, end, idx = 0, MAX, 1
  while start < end :
    mid = (start + end) // 2
    tree[idx] += 1
    if target <= mid :
      idx = idx*2
      end = mid
    else :
      idx = idx*2 + 1
      start = mid + 1
  tree[idx] += 1

def search(target) :
  start, end, idx = 0, MAX, 1
  while start < end :
    mid = (start + end) // 2
    tree[idx] -= 1
    if target <= tree[idx*2] :
      idx = idx*2
      end = mid
    else :
      target -= tree[idx*2]
      idx = idx*2 + 1
      start = mid + 1
  tree[idx] -= 1
  return end

N = int(input())
for _ in range(N) :
  t, x = map(int, input().split())
  if t == 1 :
    update(x)
  else :
    print(search(x))