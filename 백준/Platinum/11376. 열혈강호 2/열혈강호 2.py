import sys
input = sys.stdin.readline

N, M = map(int, input().split())
worker_list = [list(map(int, input().split()))[1:] for _ in range(N)]
works = [-1]*(M+1)
ans = 0

def dfs(worker) :
  if visited[worker] :
    return False
  visited[worker] = True

  for work in worker_list[worker] :
    if works[work] == -1 or dfs(works[work]) :
      works[work] = worker
      return True
  return False

for i in range(N) :
  for _ in range(2) :
    visited = [False]*(N)
    if dfs(i) :
      ans += 1

print(ans)