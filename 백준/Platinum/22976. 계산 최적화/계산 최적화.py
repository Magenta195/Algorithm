import sys
input = sys.stdin.readline
MOD = 10**9 + 7

N, Q = map(int, input().split())
ops = [input().split() for _ in range(N)]
index = [0]*N
tree = [[0]*2 for i in range(4*N)]

def init(start=0, end=N-1, idx=1) :
  if start == end :
    op, num = ops[start]
    if op == '+' :
      tree[idx] = [1, int(num)]
    else :
      tree[idx] = [int(num), 0]
    index[start] = idx
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)
  tree[idx][0] = (tree[idx*2][0] * tree[idx*2+1][0]) % MOD
  tree[idx][1] = (tree[idx*2][1] * tree[idx*2+1][0] + tree[idx*2+1][1]) % MOD

def update(idx, op, num) :
  idx = index[idx]
  if op == '+' :
    tree[idx] = [1, num]
  else :
    tree[idx] = [num, 0]
  while idx > 1 :
    idx //= 2
    tree[idx][0] = (tree[idx*2][0] * tree[idx*2+1][0]) % MOD
    tree[idx][1] = (tree[idx*2][1] * tree[idx*2+1][0] + tree[idx*2+1][1]) % MOD
    
init()
for _ in range(Q) :
  idx, op, num = input().split()
  update(int(idx)-1, op, int(num))
  print(tree[1][1])