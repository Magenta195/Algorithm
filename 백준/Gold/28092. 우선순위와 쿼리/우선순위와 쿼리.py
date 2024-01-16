import bisect
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
parents = [ x for x in range(N+1)]
nodes = [1]*(N+1)
roots = [[0]*2 for _ in range(4*N+4)]

def init(start = 0, end = N, idx = 1) :
  if start == end :
    roots[idx] = [start, 1] if start else [start, 0]
    return
  mid = (start + end) // 2
  init(start, mid, idx*2)
  init(mid+1, end, idx*2+1)
  if roots[idx*2][1] >= roots[idx*2+1][1] :
    target = idx*2
  else :
    target = idx*2+1
  for i in range(2) :
    roots[idx][i] = roots[target][i]

def update(target, val, start = 0, end = N, idx = 1) :
  if target < start or target > end :
    return
  if start == end :
    roots[idx][1] += val
    return
  mid = (start + end) // 2
  update(target, val, start, mid, idx*2)
  update(target, val, mid+1, end, idx*2+1)
  if roots[idx*2][1] >= roots[idx*2+1][1] :
    target = idx*2
  else :
    target = idx*2+1
  for i in range(2) :
    roots[idx][i] = roots[target][i]
  
def find(n) :
  ret = []
  while parents[n] != n :
    ret.append(n)
    n = parents[n]
  for r in ret :
    parents[r] = n
  return n

def union(a, b) :
  pa = find(a)
  pb = find(b)
  pan, pbn = nodes[pa], nodes[pb]
  if pa == pb or pan == -1 or pbn == -1 :
    nodes[pa] = nodes[pb] = -1
    update(pa, -pan-1)
    update(pb, -pbn-1)
    return
  if pa > pb :
    pa, pb = pb, pa
  parents[pb] = parents[pa]
  update(pb, -nodes[pb])
  update(pa, nodes[pb])
  nodes[pa] += nodes[pb]
  nodes[pb] = 0
  
init()
for _ in range(Q) :
  q, *cmd = map(int, input().split())
  if q == 1 :
    u, v = cmd
    union(u, v)
  else :
    br, bn = roots[1]
    print(br)
    nodes[br] = -1
    update(br, -bn-1)