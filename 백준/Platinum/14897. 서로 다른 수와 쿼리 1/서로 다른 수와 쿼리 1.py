from collections import defaultdict
import math
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nxt_dict = dict()
nxt_list = defaultdict(list) 
for i in range(N-1, -1, -1) :
  nxt = nxt_dict[nums[i]] if nums[i] in nxt_dict else N
  nxt_list[nxt].append(i)
  nxt_dict[nums[i]] = i

sz = 1 << math.ceil(math.log2(N+1))
tree = [0]*(2*sz)

def update(target, val) :
  target += sz 
  tree[target] += val
  while target > 1 :
    target >>= 1
    tree[target] = tree[target<<1] + tree[target<<1|1]

def search(l, r) :
  ret = 0
  l += sz
  r += sz
  while l <= r :
    if l & 1 :
      ret += tree[l]
      l += 1
    if not r & 1 :
      ret += tree[r]
      r -= 1
    l >>= 1
    r >>= 1
  return ret

Q = int(input())
ans = [0]*Q
queries = [[i] + list(map(int, input().split())) for i in range(Q)]
queries.sort(key = lambda x : -x[2])
i = N+1
for idx, l, r in queries :
  l -= 1
  r -= 1
  for j in range(r+1, i) :
    for k in nxt_list[j] :
      update(k, 1)
  i = r+1
  ans[idx] = search(l, r)
print(*ans, sep = '\n')