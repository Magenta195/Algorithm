from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
edge_dict = defaultdict(list)

def dfs(node) :
  visited = [False]*N
  visited[node] = True
  q = [node]
  cnt = 1

  while q :
    node = q.pop()
    for nxt in edge_dict[node] :
      if not visited[nxt] :
        visited[nxt] = True
        cnt += 1
        q.append(nxt)
    
  return cnt
    
for _ in range(M) :
  A, B = map(int, input().split())
  edge_dict[B-1].append(A-1)

answer, maxlen = [], 0
for i in range(N) :
  tmp = dfs(i)
  if tmp > maxlen :
    answer, maxlen = [i+1], tmp
  elif tmp == maxlen :
    answer.append(i+1)
print(*answer)