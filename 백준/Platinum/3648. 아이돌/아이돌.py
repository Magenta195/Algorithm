from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def cvt(x) :
  if x < 0 :
    return -x-1+N
  return x-1
    
def neg(x) :
  return (x + N) % (2*N)

def solve() :
  global N, idx, scc_idx
  lines = input()
  if lines == "" :
    return False
  N, M = map(int, lines.split())
  edge_dict = defaultdict(list)
  edge_dict[N].append(0)
  stk = list()
  idx, scc_idx = 0, 0
  visited = [-1]*(2*N)
  scc_result = [-1]*(2*N)

  for _ in range(M) :
    a, b = map(int, input().split())
    a = cvt(a)
    b = cvt(b)
    edge_dict[neg(a)].append(b)
    edge_dict[neg(b)].append(a)

  def dfs(node) :
    global idx, scc_idx
    visited[node] = result = idx
    idx += 1
    stk.append(node)
    for nxt in edge_dict[node] :
      if scc_result[nxt] > -1 : 
        continue
      if visited[nxt] == -1 :
        dfs(nxt)
      result = min(result, visited[nxt])
    if result == visited[node] :
      while True :
        n = stk.pop()
        scc_result[n] = scc_idx
        if n == node :
          break
      scc_idx += 1
    visited[node] = result

  for i in range(2*N) :
    if scc_result[i] == -1 :
      dfs(i)

  for i in range(N) :
    if scc_result[i] == scc_result[neg(i)] :
      print("no")
      return True
  print("yes")
  return True

while True :
  if not solve() :
    break