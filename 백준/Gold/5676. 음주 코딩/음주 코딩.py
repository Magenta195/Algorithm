import sys
input = sys.stdin.readline

def sign(n) :
  if n > 0 :
    return 1
  if n == 0 :
    return 0
  return -1

def init(N, nums, tree) :
  for i in range(N) :
    tree[i+N] = sign(nums[i])
  for i in range(N-1, -1, -1) :
    tree[i] = tree[i<<1] * tree[i<<1|1]

def update(N, tree, idx, val) :
  idx += N
  tree[idx] = sign(val)
  while idx :
    idx >>= 1
    tree[idx] = tree[idx<<1] * tree[idx<<1|1]

def query(N, tree, l, r) :
  l += N
  r += N
  res = 1
  while l <= r :
    if l % 2 == 1 :
      res *= tree[l]
      l += 1
    if r % 2 == 0 :
      res *= tree[r]
      r -= 1
    l >>= 1
    r >>= 1
  return res

def solve() :
  N, K = map(int, input().split())
  tree = [0]*(2*N)
  nums = list(map(int, input().split()))
  ans = ''
  init(N, nums, tree)
  for _ in range(K) :
    q, *cmd = input().split()
    if q == 'C' :
      i, v = map(int, cmd)
      update(N, tree, i-1, v)
    else :
      i, j = map(int, cmd)
      res = query(N, tree, i-1, j-1)
      if res == 1 :
        res = '+'
      else :
        res = '-' if res < 0 else '0'
      ans += res
  print(ans)

while True :
  try :
    solve()
  except :
    break