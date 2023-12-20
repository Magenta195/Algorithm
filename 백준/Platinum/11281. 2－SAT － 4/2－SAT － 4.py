from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
MAX = float('inf')

N, M = map(int, input().split())
edge_dict = defaultdict(list)

def cvt(a) :
  if a < 0 :
    return -a-1+N
  else :
    return a-1

def neg(a) :
  return (a + N) % (2*N)

for _ in range(M) :
  a, b = map(int, input().split())
  a = cvt(a)
  b = cvt(b)
  edge_dict[neg(a)].append(b)
  edge_dict[neg(b)].append(a)

visited = [MAX]*(2*N)
finished = [False]*(2*N)
stk = list()
scc_result = [-1]*(2*N)
idx, scc_idx = 0, 0

def scc(node) :
  global idx, scc_idx
  visited[node] = result = idx
  idx += 1
  stk.append(node)

  for nxt in edge_dict[node] :
    if finished[nxt] :
      continue
    if visited[nxt] < MAX :
      result = min(result, visited[nxt])
      continue
    result = min(result, scc(nxt))

  if result == visited[node] :
    while stk :
      n = stk.pop()
      finished[n] = True
      scc_result[n] = scc_idx
      if n == node :
        break
    scc_idx += 1
  return result

for i in range(2*N) :
  if not finished[i] :
    scc(i)

result = [0]*N
for i in range(N) :
  if scc_result[i] == scc_result[neg(i)] :
    print(0)
    exit()
  if scc_result[i] < scc_result[neg(i)] :
    result[i] = 1
print(1)
print(*result[:N])